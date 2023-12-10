import socket
import pyautogui as au

server = socket.socket()
server.bind(("localhost", 12))
server.listen(1)

# while True:
#     client,InetAddress = server.accept()
#     client.send(bytes("12", "utf-8"))


while True:
    print(au.position())