print("-------Shortest Job First Scheduling (Non Pre-emptive)--------")
n = int(input("Enter the number of Processes: "))

p = [i + 1 for i in range(n)]  # Process IDs
bt = []  # Burst times
at = []  # Arrival times
wt = [0] * n  # Waiting times
tt = [0] * n  # Turnaround times
ta = 0
wsum = 0.0
tsum = 0.0

# Input burst time and arrival time for each process
for i in range(n):
    bt.append(int(input(f"Enter the burst time of process {i + 1}: ")))
    at.append(int(input(f"Enter the arrival time of process {i + 1}: ")))

# Sorting processes by arrival time
for i in range(n):
    for j in range(i + 1, n):
        if at[i] > at[j]:
            p[i], p[j] = p[j], p[i]
            at[i], at[j] = at[j], at[i]
            bt[i], bt[j] = bt[j], bt[i]

btime = 0
k = 0

# Scheduling processes based on burst time after sorting by arrival time
for j in range(n):
    btime += bt[j]
    min_bt = bt[k]
    for i in range(k + 1, n):
        if btime >= at[i] and bt[i] < min_bt:
            p[k + 1], p[i] = p[i], p[k + 1]
            at[k + 1], at[i] = at[i], at[k + 1]
            bt[k + 1], bt[i] = bt[i], bt[k + 1]
            min_bt = bt[k + 1]
    k += 1

# Calculating waiting times and turnaround times
for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1] - at[i] + at[i - 1]
    if wt[i] < 0:  # Ensure waiting time isn't negative
        wt[i] = 0
    wsum += wt[i]

for i in range(n):
    tt[i] = wt[i] + bt[i]
    tsum += tt[i]

# Average waiting time and turnaround time
wavg = wsum / n
tavg = tsum / n

# Output the results
print("***************************")
print("OUTPUT:-")
print("Process\t Burst\t Arrival\t Waiting\t TurnAround")
for i in range(n):
    print(f"P{p[i]}\t {bt[i]}\t {at[i]}\t\t {wt[i]}\t\t {tt[i]}")

print("\nAverage Waiting Time:", round(wavg, 2))
print("Average TurnAround Time:", round(tavg, 2))
