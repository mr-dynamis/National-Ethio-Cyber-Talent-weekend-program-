import argparse
import asyncio

from core.engine import ScanEngine
from core.fingerprint import detect_os
from utils.resolver import resolve

from plugins import http_title, ssh_version


# -----------------------------
# Detailed Scan Function
# -----------------------------
async def detailed_scan(target, port, results, verbose=False):
    try:
        conn = asyncio.open_connection(target, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)

        results.append((port, "OPEN", "TCP"))
        writer.close()
        await writer.wait_closed()

    except asyncio.TimeoutError:
        results.append((port, "FILTERED", "TCP"))

    except ConnectionRefusedError:
        results.append((port, "CLOSED", "TCP"))

    except Exception as e:
        if verbose:
            print(f"[DEBUG] Port {port} error: {e}")
        results.append((port, "FILTERED", "TCP"))


# -----------------------------
# Load Plugins
# -----------------------------
def load_plugins():
    return [
        ("HTTP", http_title),
        ("SSH", ssh_version)
    ]


# -----------------------------
# Main Function
# -----------------------------
async def main():
    parser = argparse.ArgumentParser(description="Mini Nmap Scanner (Improved)")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", default="1-100", help="Port range (e.g. 1-100)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")

    args = parser.parse_args()

    start, end = map(int, args.p.split("-"))
    ports = list(range(start, end + 1))

    ip = resolve(args.target)

    print("=" * 50)
    print(f"[+] Target      : {args.target}")
    print(f"[+] IP Address  : {ip}")
    print(f"[+] Port Range  : {start}-{end}")
    print("=" * 50)

    # OS Detection
    os_guess = detect_os(ip)
    print(f"[+] OS Guess: {os_guess}")
    print("=" * 50)

    # Run scan
    engine = ScanEngine(ip, ports)

    tasks = [
        detailed_scan(ip, port, engine.results, args.verbose)
        for port in ports
    ]

    await asyncio.gather(*tasks)

    # Load plugins
    plugins = load_plugins()

    print("\n[+] Scan Results:\n")

    open_found = False

    for port, status, method in sorted(engine.results):

        # Show OPEN ports
        if status == "OPEN":
            open_found = True
            print(f"[OPEN]     Port {port}")

            # Run plugins
            for name, plugin in plugins:
                if args.verbose:
                    print(f"   [DEBUG] Running {name} plugin...")

                result = plugin.run(ip, port)

                if result:
                    print(f"   └── {result}")
                elif args.verbose:
                    print(f"   └── No {name} data")

        # Show CLOSED ports (always)
        elif status == "CLOSED":
            print(f"[CLOSED]   Port {port}")

        # Show FILTERED only in verbose
        elif status == "FILTERED" and args.verbose:
            print(f"[FILTERED] Port {port}")

    # If no open ports found
    if not open_found:
        print("\n[!] No open ports found in this range.")

    print("\n[+] Scan Complete")
    print("=" * 50)


# Run program
if __name__ == "__main__":
    asyncio.run(main())
