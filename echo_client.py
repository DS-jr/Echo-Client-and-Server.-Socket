import socket

HOST = "127.0.0.1"  # Server's hostname or IP address
PORT = 5432  # Port used by the server


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP
        s.connect((HOST, PORT))
        while True:
            input_in_bytes = str.encode(input('Type some word & press "Enter" (to exit - press "Ctr+C"): '))
            s.sendall(input_in_bytes)
            data = s.recv(1024)
            print(f"Client received back from Server: {data}")


if __name__ == '__main__':
    main()
