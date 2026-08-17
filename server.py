import socket
from urllib import response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is listening on port 5000...")

conn, addr = server.accept()
print(f"Connected {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    print("Client", data)

    response = "Received: " + data
    conn.send(response.encode())