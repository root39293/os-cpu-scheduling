import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class Process:
    def __init__(self, name, arrivalTime, burstTime):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.startTime = [0]
        self.completionTime = 0
        self.waitTime = 0
        self.remainingTime = burstTime
        self.turnAroundTime = 0
        self.preempted = False  
        self.preemptedTime = 0

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



def RoundRobin(processes, timeSlice):
    readyQueue = Queue()
    for process in processes:
        readyQueue.enqueue(process)

    executionQueue = Queue()
    currentTime = 0
    executedProcesses = []
    while not readyQueue.isEmpty() or not executionQueue.isEmpty():
        while not readyQueue.isEmpty() and readyQueue.items[0].arrivalTime <= currentTime:
            executionQueue.enqueue(readyQueue.dequeue())

        if executionQueue.isEmpty():
            currentTime += 1
            continue

        process = executionQueue.dequeue()
        if process.remainingTime > timeSlice:
            process.preempted = True
            process.preemptedTime = timeSlice
            process.startTime.append(currentTime)
            process.remainingTime -= timeSlice
            currentTime += timeSlice
            readyQueue.enqueue(process)
        else:
            process.startTime.append(currentTime)
            currentTime += process.remainingTime
            process.remainingTime = 0
            process.completionTime = currentTime
            process.turnAroundTime = process.completionTime - process.arrivalTime
            process.waitTime = process.turnAroundTime - process.burstTime
            executedProcesses.append(process)

    executedProcesses.sort(key=lambda x: x.arrivalTime)
    return executedProcesses



def ganttChart(processes, timeSlice):
    fig, ax = plt.subplots()
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    yticks = []
    ytick_labels = []

    process_positions = {}

    for process in processes:
        if process.name not in process_positions:
            process_positions[process.name] = len(process_positions)
        
        y_pos = process_positions[process.name]
        for idx, start_time in enumerate(process.startTime):
            if process.preempted and idx < len(process.startTime) - 1:
                end_time = start_time + timeSlice
            else:
                end_time = process.completionTime
            
       
            if start_time >= process.arrivalTime:
                ax.broken_barh([(start_time, end_time - start_time)], (y_pos-0.4, 0.8), facecolors='blue')
        
    yticks = list(range(len(process_positions)))
    ytick_labels = sorted(process_positions, key=process_positions.get)

    ax.set_yticks(yticks)
    ax.set_yticklabels(ytick_labels)
    

    ax.xaxis.set_major_locator(MultipleLocator(2))
    
    ax.grid(True)
    plt.title("Gantt Chart for Round Robin")
    plt.show()








def main():
    num = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num):
        arrivalTime = int(input(f"Enter the arrival time of process P{i + 1}: "))
        burstTime = int(input(f"Enter the burst time of process P{i + 1}: "))
        process = Process(f"P{i + 1}", arrivalTime, burstTime)
        processes.append(process)
    timeSlice = int(input("Enter the number of timeSlice: "))
    executedProcesses = RoundRobin(processes,timeSlice)
    
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
    ganttChart(executedProcesses, timeSlice)

if __name__ == '__main__':
    main()
    input("Press Enter key to exit...")



