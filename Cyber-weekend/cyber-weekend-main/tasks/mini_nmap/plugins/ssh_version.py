import socket

def run(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))

        banner = sock.recv(1024).decode().strip()
        return f"SSH: {banner}"

    except:
        return None
