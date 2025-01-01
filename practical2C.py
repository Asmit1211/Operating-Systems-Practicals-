n = int(input("Enter the number of terms:"))

fib0 = 0
fib1 = 1

print("fibonacci Series:",end=" ")

for i in range(1, n+1):
    print(fib0,end=" ")
    fibn = fib0 + fib1
    fib0 = fib1
    fib1 = fibn
    
print()