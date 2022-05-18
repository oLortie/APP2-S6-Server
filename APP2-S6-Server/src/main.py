import socket

HOST = "0.0.0.0"
PORT = 8888

if __name__ == "__main__":
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                print("allo")
                data = conn.recv(1024)
                if not data:
                    break
                print(data)