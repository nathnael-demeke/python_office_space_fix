import socket
import pyautogui
import json
import multiprocessing as mp

pyautogui.FAILSAFE = False

# client.connect(("192.168.1.10", 12))


clientWindowWidth = pyautogui.size().width
clientWindowHeight = pyautogui.size().height

try: 
   config_file = open("settings.json")
   configurations = json.load(config_file)
   server_address = configurations["ServerAddress"]
except Exception as e:
   print("Please Configure your adresses in 'settings.json'")
   print(e)
finally:
   def recive_key_pressed():
      key_pressed_socket = socket.socket()
      key_pressed_socket.connect((server_address, 10))
      print("key events have started...")
      while True:
         key_event = key_pressed_socket.recv(1024).decode("utf-8")
         if key_event == "Key.enter":
            pyautogui.press("enter")
         elif key_event == "Key.backspace":
            pyautogui.press("backspace")
         elif key_event == "Key.space":
            pyautogui.press("space")
         else:
            pyautogui.press(key_event)
            print(key_event)
   def recive_mouse_clicked():
      print("Recive mouse event started")
      mouse_event_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      mouse_event_client.bind(("0.0.0.0" , 100))
      mouse_event_client.listen(10)
      
      while True:
         cli,addr = mouse_event_client.accept()
         event = cli.recv(1024).decode("utf-8")
         if event == "clicked":
            pyautogui.click()
            try:
               cli.close()
            except:
               print("err")
         elif event == "scrollDown":
               pyautogui.scroll(3)
               pass
         elif event == "scrollUp":
            pass

   def recieve_mouse_location():
      print("started")
      client = socket.socket()
      client.connect((server_address, 20))
      init_message = client.recv(1024).decode('utf-8')
      init_message = json.loads(init_message)
      serverWindowWidth = init_message["WindowWidth"]
      serverWindowHeight = init_message["WindowHeight"]
      #The factor variables are the one that we will use to make some adjustments on different screen sized computers
      width_factor = serverWindowWidth / clientWindowWidth
      height_factor = serverWindowHeight / clientWindowHeight
      print(f"windows width {serverWindowWidth} height {serverWindowHeight}")

      while True:
         try:     
            list =  client.recv(1024).decode("utf-8").split()
            if list != []:
               pyautogui.moveTo(int(list[0]) * width_factor, int(list[1]) * height_factor)
               print(list)   
         except Exception as mouse_location_error:
            print(mouse_location_error)

   if __name__ == '__main__':
      parralel_mouse_location = mp.Process(target=recieve_mouse_location)
      parralel_mouse_event = mp.Process(target=recive_mouse_clicked)
      parralel_key_pressed = mp.Process(target=recive_key_pressed)
      parralel_key_pressed.start()
      parralel_mouse_location.start()
      parralel_mouse_event.start()
