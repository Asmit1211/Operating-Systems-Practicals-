def main():
    count, time, remain, flag = 0, 0, 0, 0
    time_quantum = 0
    wait_time, turnaround_time = 0, 0
    at = []  # Arrival time
    bt = []  # Burst time
    rt = []  # Remaining time

    # Input number of processes
    n = int(input("Enter the total number of processes: "))
    remain = n

    # Input arrival time and burst time for each process
    for i in range(n):
        print(f"Enter Arrival Time and Burst Time for Process {i + 1}:")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        at.append(arrival)
        bt.append(burst)
        rt.append(burst)

    # Input time quantum
    time_quantum = int(input("Enter Time Quantum: "))
    print("\nProcess\t| Turnaround Time | Waiting Time")

    # Scheduling
    while remain > 0:
        for i in range(n):
            if rt[i] > 0:
                if rt[i] <= time_quantum:
                    time += rt[i]
                    rt[i] = 0
                    flag = 1
                else:
                    time += time_quantum
                    rt[i] -= time_quantum

                if rt[i] == 0 and flag == 1:
                    remain -= 1
                    turnaround = time - at[i]
                    waiting = turnaround - bt[i]
                    print(f"P[{i + 1}]\t|\t{turnaround}\t\t|\t{waiting}")
                    wait_time += waiting
                    turnaround_time += turnaround
                    flag = 0

    # Output average waiting time and turnaround time
    print(f"\nAverage Waiting Time = {wait_time / n:.2f}")
    print(f"Average Turnaround Time = {turnaround_time / n:.2f}")


if __name__ == "__main__":
    main()
