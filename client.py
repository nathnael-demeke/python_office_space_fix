import socket
import pyautogui
import multiprocessing as mp

pyautogui.FAILSAFE = False

# client.connect(("192.168.1.10", 12))


server_address = "localhost"
def recive_key_pressed():
   key_pressed_socket = socket.socket()
   key_pressed_socket.connect((server_address, 10))            
   print("key events have started...")
   while True:
      key_event = key_pressed_socket.recv(1024).decode("utf-8")
      try:
         if key_event == "Key.caps_lock":
            pyautogui.press("capslock")
            print("caps_lock has been pressed")
         elif key_event == "Key.ctrl_r" or key_event == "Key.ctrl_r":
            pyautogui.hotkey('ctrl')
            print("you have pressed the ctrl key")
         else:
           pyautogui.press("{0}".format(key_event))
         pyautogui.press(key_event)               
         print("{0}".format(key_event))  
      except Exception as e:
         print(e)
def recive_mouse_clicked():
   mouse_event_client = socket.socket()
   mouse_event_client.connect((server_address , 80))
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
        client.connect((server_address, 20))
        list =  client.recv(1024).decode("utf-8").split()
        pyautogui.moveTo(int(list[0]), int(list[1]))
        print(list)

        client.close()

if __name__ == '__main__':
   parralel_mouse_location = mp.Process(target=recieve_mouse_location)
   parralel_mouse_event = mp.Process(target=recive_mouse_clicked)
   parralel_key_pressed = mp.Process(target=recive_key_pressed)
   parralel_key_pressed.start()
   parralel_mouse_location.start()
   parralel_mouse_event.start()
