mutex = 1
full = 0
empty = 3
x = 0

def wait(s):
    return s - 1

def signal(s):
    return s + 1

def producer1():
    global mutex,full,empty,x
    mutex = wait(mutex)
    full = signal(full)
    empty = wait(empty)
    x += 1
    print(f"\nProducer produces the item {x}")
    mutex = signal(mutex)

def consumer1():
    global mutex,full,empty,x
    mutex = wait(mutex)
    full = wait(full)
    empty = signal(empty)
    print(f"\nConsumer consumes the item{x}")
    x -= 1
    mutex = signal(mutex)

while True:
    print("\n1. Producer\n2. Consumer\n3. Exit")
    n = int(input("\nEnter your choice:"))
    if n == 1:
        if mutex == 1 and empty !=0:
            producer1()
        else:
            print("Buffer is full !")
    elif n == 2:
        if mutex == 1 and full !=0:
            consumer1()
        else:
            print("Buffer is empty")
    elif n == 3:
        break