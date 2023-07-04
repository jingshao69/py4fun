#!/usr/bin/env python3

import socket
import sys

# We need to support both IPv4 and IPv6
def bindServerPort(port):
    info = socket.getaddrinfo("::", port, socket.AF_UNSPEC, socket.SOCK_STREAM,
                0, socket.AI_PASSIVE)
    err = None
    for res in info:
        af, socktype, proto, canonname, sa = res
        sock = None
        try:
            sock = socket.socket(af, socktype, proto)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Disable IPV6_ONLY on AF_INET6
            if af == socket.AF_INET6:
                sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            print("%d bind!" %(port))
            sock.bind(sa)
           
            return sock
        except socket.error as _:
            err = _
            if sock is not None:
                sock.close()
    if err is not None:
        raise err
    else:
        raise socket.error("getaddrinfo returns an empty list")


if __name__ == "__main__":
    sock = bindServerPort(8008);
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if len(data) > 0:
                print("Recvd: %s" %(data.decode('utf-8')))
            if not data: 
                break
            conn.send(data)
        conn.close()

