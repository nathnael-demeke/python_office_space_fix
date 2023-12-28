import socket
import pyautogui
import multiprocessing as mp

pyautogui.FAILSAFE = False

# client.connect(("192.168.1.10", 12))



server_address = "localhost"

def recive_mouse_clicked():
   mouse_event_client = socket.socket()
   mouse_event_client.connect((server_address
                               , 110))
   while True:
      clicked = mouse_event_client.recv(1024).decode("utf-8")
      if clicked == "yes":
         pyautogui.click()
         print("recived")

      else:
         pass
      

def recieve_mouse_location():
    while True:
        client = socket.socket()
        client.connect((server_address, 112))
        list =  client.recv(1024).decode("utf-8").split()
        pyautogui.moveTo(int(list[0]), int(list[1]))
        print(list)

        client.close()

if __name__ == '__main__':
   parralel_mouse_location = mp.Process(target=recieve_mouse_location)
   parralel_mouse_event = mp.Process(target=recive_mouse_clicked)
   parralel_mouse_location.start()
   parralel_mouse_event.start()
