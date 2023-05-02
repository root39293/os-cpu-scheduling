
import matplotlib.pyplot as plt

class Process:
    def __init__(self, name, arrivalTime, burstTime):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.startTime = 0
        self.completionTime = 0
        self.waitTime = 0

    def __repr__(self):
        return f"Process {self.name} (Arrival Time: {self.arrivalTime}, Burst Time: {self.burstTime}, Start Time: {self.startTime}, Completion Time: {self.completionTime}, Wait Time: {self.waitTime})"

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0


def gantChart(processes):
    fig, ax = plt.subplots()

    ax.set_xlabel('Time')
    ax.set_ylabel('Processes')

    ax.set_xlim(0, processes[-1].completionTime)
    ax.set_xticks([i for i in range(0, processes[-1].completionTime + 1, 2)])
    ax.set_ylim(0, len(processes)+1)
    ax.set_yticks([i+0.5 for i in range(len(processes))])
    ax.set_yticklabels([processes[i].name for i in range(len(processes))])

    for i in range(len(processes)):
        process = processes[i]
        ax.broken_barh([(process.startTime, process.burstTime)], (i+0.1, 0.8))

    ax.set_title('Gantt Chart for FCFS')
    ax.grid(True)
    plt.show()


def FCFS(processes):
    readyQueue = Queue()
    for process in processes:
        readyQueue.enqueue(process)

    readyQueue.items.sort(key=lambda x: x.arrivalTime)
    executionQueue = Queue()

    currentTime = 0
    while not readyQueue.isEmpty():
        process = readyQueue.dequeue()
        while currentTime < process.arrivalTime:
            currentTime += 1
        executionQueue.enqueue(process)
        process.startTime = currentTime
        currentTime += process.burstTime
        process.completionTime = currentTime
        process.waitTime = process.startTime - process.arrivalTime

    executedProcesses = []
    while not executionQueue.isEmpty():
        executedProcesses.append(executionQueue.dequeue())

    return executedProcesses


def main():
    num = int(input("Enter the number of processes: "))

    processes = []
    for i in range(num):
        arrivalTime = int(input(f"Enter the arrival time of process P{i + 1}: "))
        burstTime = int(input(f"Enter the burst time of process P{i + 1}: "))
        process = Process(f"P{i + 1}", arrivalTime, burstTime)
        processes.append(process)

    executedProcesses = FCFS(processes)

    totalWaitingTime = 0
    for process in executedProcesses:
        totalWaitingTime += process.waitTime

    averageWaitingTime = totalWaitingTime / len(executedProcesses)
    print("Executed Processes:")
    print("{:<10}  {:<15}  {:<15}  {:<15}  {:<15}  {:<15}".format("Name", "Arrival Time", "Burst Time", "Start Time", "Completion Time", "Wait Time"))
    for process in executedProcesses:
        print("{:<10}  {:<15}  {:<15}  {:<15}  {:<15}  {:<15}".format(process.name, process.arrivalTime, process.burstTime, process.startTime, process.completionTime, process.waitTime))
    print(f"Average Waiting Time: {averageWaitingTime}")

    gantChart(executedProcesses)



if __name__ == "__main__":
    main()
    input("Press Enter key to exit...")


