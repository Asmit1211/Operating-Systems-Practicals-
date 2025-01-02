import threading
import time
import random

BUFFER_SIZE = 5
buffer = []
buffer_lock = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

class Producer(threading.Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1, 10)
            empty.acquire()
            buffer_lock.acquire()
            buffer.append(item)
            print(f"Produced item: {item}. Buffer: {buffer}")
            buffer_lock.release()
            full.release()
            time.sleep(random.uniform(0.5, 2))

class Consumer(threading.Thread):
    def run(self):
        global buffer
        while True:
            full.acquire()
            buffer_lock.acquire()
            item = buffer.pop(0)
            print(f"Consumed item: {item}. Buffer: {buffer}")
            buffer_lock.release()
            empty.release()
            time.sleep(random.uniform(0.5, 2))

def main():
    print("Starting producer and consumer threads")
    
    producer_threads = [Producer() for _ in range(2)]
    consumer_threads = [Consumer() for _ in range(2)]

    for producer in producer_threads:
        producer.start()
    for consumer in consumer_threads:
        consumer.start()
    
    # Let the threads run for 10 seconds
    time.sleep(10)
    
    print("Main thread exiting...")

if __name__ == "__main__":
    main()