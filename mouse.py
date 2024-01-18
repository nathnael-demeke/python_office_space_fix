from pynput.mouse import *
def send_mouse_clicked():    
   print("send_mouse_clicked() has began") 
   def on_click(x, y, button, pressed):  
      print("you have clicked")
      if pressed == True:
            try:
               
                  print("you hace passed line 48")
                  # cli.send(bytes("yes", "utf-8"))          
                
            except Exception as e :
              print(e)
   with Listener(on_click=on_click) as listener:
        listener.join()   
while True:
    send_mouse_clicked()