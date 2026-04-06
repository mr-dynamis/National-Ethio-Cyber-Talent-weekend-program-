import socket

def run(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        sock.send(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")

        data = sock.recv(4096).decode(errors="ignore")

        if "<title>" in data:
            title = data.split("<title>")[1].split("</title>")[0]
            return f"HTTP Title: {title}"

    except:
        return None
