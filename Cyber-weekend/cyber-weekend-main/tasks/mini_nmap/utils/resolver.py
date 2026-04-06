import socket

def resolve(target):
    return socket.gethostbyname(target)
