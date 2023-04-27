class Process:
    def __init__(self, name, arrivalTime, burstTime):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.startTime = 0
        self.completionTime = 0
        self.waitTime = 0
    
    def __repr__(self):
        return f"Process {self.name} (Arrival Time: {self.arrivalTime}, Burst Time: {self.burstTime}, Start Time: {self.startTime}, Completion Time: {self.completionTime})"

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

def SJF(processes):
    readyQueue = Queue()
    for process in processes:
        readyQueue.enqueue(process)

    executionQueue = Queue()

    currentTime = 0
    while not readyQueue.isEmpty():
        readyQueue.items.sort(key=lambda x: x.burstTime)
        process = readyQueue.dequeue()
        while currentTime < process.arrivalTime:
            currentTime += 1
        executionQueue.enqueue(process)
        process.startTime = currentTime
        currentTime += process.burstTime
        process.completionTime = currentTime

    executedProcesses = []
    while not executionQueue.isEmpty():
        executedProcesses.append(executionQueue.dequeue())

    return executedProcesses

def main():
    num = int(input('Enter the number of processes: '))

    processes = []
    for i in range(num):
        arrivalTime = int(input(f'Enter the arrival time of process P{i + 1}: '))
        burstTime = int(input(f'Enter the burst time of process P{i + 1}: '))
        process = Process(f'P{i + 1}', arrivalTime, burstTime)
        processes.append(process)

    executedProcesses = SJF(processes)

    totalWaitingTime = 0
    for process in executedProcesses:
        waitingTime = process.startTime - process.arrivalTime
        totalWaitingTime += waitingTime

    averageWaitingTime = totalWaitingTime / len(executedProcesses)
    print("Executed Processes:")
    print("{:<10}  {:<15}  {:<15}  {:<15}  {:<15}".format("Name", "Arrival Time", "Burst Time", "Start Time", "Completion Time"))
    for process in executedProcesses:
        print("{:<10}  {:<15}  {:<15}  {:<15}  {:<15}".format(process.name, process.arrivalTime, process.burstTime, process.startTime, process.completionTime))
    print(f"Average Waiting Time: {averageWaitingTime}")

if __name__ == '__main__':
    main()
    input("Press Enter key to exit...")