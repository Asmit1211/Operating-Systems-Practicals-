MAXSIZE = 10
def main():
    array = [0] * MAXSIZE
    num = int(input("Enter the value of N : "))
    print("Enter",num,"Numbers (-ve,+ve and zero):")
    for i in range(num):
        array[i] = int(input())
    
    print("Input array element:")
    for i in range(num):
        print("{:+3d}".format(array[i]))
        
    negative_sum = 0
    positive_sum = 0
    total=0.0
    
    for i in range(num):
        if array[i]<0:
            negative_sum += array[i]
        elif array[i] > 0 :
            positive_sum += array[i]
            total += array[i]
        avearge = total / num
        print("\nSum of negative numbers: ", negative_sum)
        print("\nSum of positive numbers: ", positive_sum)
        print("Average of all input numbers = {:.2f}".format(avearge))

if __name__=="__main__":
    main()
           