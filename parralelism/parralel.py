import time


then = time.time()
def square(number):
       print(number ** 2)

    
def full_process():
    for i in range(1200):
       square(i)
full_process()
full_process()
full_process()
full_process()
full_process()
full_process()
full_process()
full_process()
full_process()
full_process()
full_process()


now = time.time()
print(f"This is time {now - then}")


