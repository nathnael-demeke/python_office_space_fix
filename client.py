import socket


while True:
    client = socket.socket()
    client.connect(("localhost", 12))

    print(client.recv(1024).decode("utf-8"))
