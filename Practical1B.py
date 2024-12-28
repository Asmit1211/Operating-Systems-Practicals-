from threading import Condition,Thread
import random
import time

Condition = Condition()
queue = []

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            Condition.acquire()
            if not queue:
                print("Nothing in queue,consumer is waiting")
                Condition.wait()
                print("Producer added something to queue and notified the consumer")
            num = queue.pop(0)
            print("Consumer",num)
            Condition.release()
            time.sleep(random.random())

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            Condition.acquire()
            num = random.choice(nums)
            queue.append(num)
            print("Produced",num)
            Condition.notify()
            Condition.release()
            time.sleep(random.random())
ProducerThread().start()
ConsumerThread().start()