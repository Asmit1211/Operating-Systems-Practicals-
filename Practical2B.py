def main():
    l = int(input("Enter the limit : "))
    if l < 2:
        print("No prime numbers less than 2")
        return
    
    nlist = [i for i in range(l + 1)]  # Initialize with numbers from 0 to l
    temp = 0
    
    for i in range(2, l + 1):
        if nlist[i] != 0:
            t = i
            p = nlist[i]
            while (t + p) <= l:
                nlist[t + p] = 0
                t += p
    
    # Print remaining non-zero values (prime numbers)
    for i in range(2, l + 1):
        if nlist[i] != 0:
            print(nlist[i], end=" ")

if __name__ == "__main__":
    main()
