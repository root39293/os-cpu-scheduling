import matplotlib.pyplot as plt

class Process:
    def __init__(self, name, arrivalTime, burstTime):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.startTime = 0
        self.completionTime = 0
        self.waitTime = 0
        self.remainingTime = burstTime
        self.turnAroundTime = 0

    def __repr__(self):
        return f"Process(name='{self.name}', arrivalTime={self.arrivalTime}, burstTime={self.burstTime})"
    
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
    
def HRRN(processes):
    readyQueue = Queue()
    executionQueue = Queue()
    ratioQueue = Queue()
    currentTime = 0

    for process in processes:
        readyQueue.enqueue(process)

    while not readyQueue.isEmpty():
        hrrnProcess = None
        hrrnValue = -1
        for process in readyQueue.items:
            responseRatio = (currentTime - process.arrivalTime + process.burstTime) / process.burstTime
            if responseRatio > hrrnValue:
                hrrnValue = responseRatio
                hrrnProcess = process

        readyQueue.items.remove(hrrnProcess)
        executionQueue.enqueue(hrrnProcess)

        if currentTime < hrrnProcess.arrivalTime:
            currentTime = hrrnProcess.arrivalTime

        hrrnProcess.startTime = currentTime
        currentTime += hrrnProcess.burstTime
        hrrnProcess.completionTime = currentTime
        hrrnProcess.turnAroundTime = hrrnProcess.completionTime - hrrnProcess.arrivalTime
        hrrnProcess.waitTime = hrrnProcess.turnAroundTime - hrrnProcess.burstTime

        ratioQueue.enqueue(hrrnProcess)
        executionQueue.dequeue()

    executedProcesses = []
    while not ratioQueue.isEmpty():
        executedProcesses.append(ratioQueue.dequeue())

    executedProcesses.sort(key=lambda x: x.arrivalTime)
    return executedProcesses


def main():
    num = int(input("Enter the number of processes: "))

    processes = []
    for i in range(num):
        arrivalTime = int(input(f"Enter the arrival time of process P{i + 1}: "))
        burstTime = int(input(f"Enter the burst time of process P{i + 1}: "))
        process = Process(f"P{i + 1}", arrivalTime, burstTime)
        processes.append(process)

    executedProcesses = HRRN(processes)

    totalWaitingTime = 0
    totalTurnAroundTime = 0
    for process in executedProcesses:
        totalWaitingTime += process.waitTime
        totalTurnAroundTime += process.turnAroundTime

    averageTurnAroundTime = totalTurnAroundTime / len(executedProcesses)
    averageWaitingTime = totalWaitingTime / len(executedProcesses)

    print("Executed Processes:")
    print("{:<10}  {:<15}  {:<15}  {:<15}  {:<15} {:<15}  ".format("Name", "Arrival Time", "Burst Time", "Completion Time", "TurnAround Time", "Wait Time" ))
    for process in executedProcesses:
        print("{:<10}  {:<15}  {:<15}  {:<15}  {:<15} {:<15}  ".format(process.name, process.arrivalTime, process.burstTime, process.completionTime, process.turnAroundTime, process.waitTime))
    print(f"Average TurnAround Time: {averageTurnAroundTime}")
    print(f"Average Waiting Time: {averageWaitingTime}")
    #ganttChart(executedProcesses)



if __name__ == "__main__":
    main()
    input("Press Enter key to exit...")
