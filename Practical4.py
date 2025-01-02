n = int(input("Enter total number of processes (maximum 20): "))
bt = []
wt = [0] * n
tat = [0] * n
avwt = 0
avtat = 0

print("\n Enter Process Burst Time")
for i in range(n):
    bt.append(int(input(f"p[{i+1}]: ")))

for i in range(1,n):
    for j in range(i):
        wt[i] += bt [j]

print("\nProcess\t\tBurst Time\tWaiting Time\tTurnAround Time")
for i in range(n):
    tat[i] = bt[i] +wt[i]
    avwt += wt[i]
    avtat += tat[i]
    print(f"P[{i+1}] \t\t {bt[i]} \t\t{wt[i]} \t\t {tat[i]}")
avwt //= n
avtat //= n
print(f"\nAverage Waiting Time: {avwt}")
print(f"Average TurnAround Time : {avtat}")