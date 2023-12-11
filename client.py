import socket
import pyautogui
import multiprocessing as mp

pyautogui.FAILSAFE = False

# client.connect(("192.168.1.10", 12))




def recive_mouse_clicked():
      mouse_event_client = socket.socket()
      mouse_event_client.connect(("localhost", 10))
      clicked = mouse_event_client.recv(1024).decode("utf-8")
      if clicked == "yes":
         pyautogui.click()
         print("clicked.")
         mouse_event_client.close()
      else:
          mouse_event_client.close()
    

while True:
        client = socket.socket()
        client.connect(("localhost", 112))
        list =  client.recv(1024).decode("utf-8").split()
        pyautogui.moveTo(int(list[0]), int(list[1]))
        print(list)

        client.close()
