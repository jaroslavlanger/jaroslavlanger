import threading
import time

def print_hello():
    time.sleep(1)
    print('Hello')
    time.sleep(1)
    {{}}

def print_world():
    time.sleep(2)
    print('world!')

t1 = threading.Thread(target=print_hello)
t1.start()
print('... first thread was started.')
t2 = threading.Thread(target=print_world, daemon=True)
t2.start()
print('... second thread was started.')
time.sleep(1)
print('Five seconds wait for the exception.')
time.sleep(5)
print('The end.')
t1.join()
