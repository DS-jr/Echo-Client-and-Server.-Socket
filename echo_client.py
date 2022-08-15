import socket

HOST = "127.0.0.1"  # Server's hostname or IP address
PORT = 5432  # Port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP 
    s.connect((HOST, PORT))
    s.sendall(b"Accept, Reality")
    data = s.recv(1024)

print(f"Received {data!r}")
