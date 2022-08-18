import socket

HOST = "127.0.0.1"  # Localhost
PORT = 5432  # Port to listen 


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print(f"Server connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            print(f"Server received from Client: {data}")


if __name__ == '__main__':
    main()
