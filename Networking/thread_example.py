from threading import Thread
from threading import Lock
import time

counter = 0
counter_lock = Lock()

def count5(thread_id: int, count: int):
    global counter
    for i in range(count):
        # counter_lock.acquire()
        # counter += 1
        # counter_lock.release()
        with counter_lock:
            counter += 1
        print(f'Thread {thread_id}: {i+1}')
        time.sleep(1)

threads = []
for i in range(5):
    t = Thread(target=count5, args=(i, i+1))
    threads.append(t)
    t.start()

for index, t in enumerate(threads):
    print(f'Odotetaan threadia {index}')
    t.join()
    print(f'Thread {index} on loppunut')

print('Main thread loppuu')
print(f'{counter = }')

