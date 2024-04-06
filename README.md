# OS CPU Scheduling

## Table of Contents

- [Overview](#overview)
- [Development Environment](#development-environment)
- [Implementation](#implementation)
- [Usage](#usage)

# Overview

This project aims to implement CPU scheduling with Python.

# Development Environment

- Language: Python 
- Runtime: Python 3.10.11
- IDE: Visual Studio Code v1.56.2
- Required packages: matplotlib

# Implementation

In this project, we will implement several CPU scheduling techniques and analyze the test results. We will use Python to implement the program and analyze the results.

The scheduling algorithms I have chosen are FCFS, SJF, Round Robin, HRRN


## 1. FCFS (First-Come First-Served)
```python
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
``` 

## 2. Shortest Job First (Non-preemptive)

```python
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
        process.waitTime = process.startTime - process.arrivalTime

    executedProcesses = []
    while not executionQueue.isEmpty():
        executedProcesses.append(executionQueue.dequeue())

    return executedProcesses
```

## 3. Round-Robin
```python
def RoundRobin(processes, timeSlice):
    readyQueue = Queue()
    for process in processes:
        readyQueue.enqueue(process)

    executionQueue = Queue()
    currentTime = 0
    executedProcesses = []
    while not readyQueue.isEmpty() or not executionQueue.isEmpty():
        while (
            not readyQueue.isEmpty() and readyQueue.items[0].arrivalTime <= currentTime
        ):
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

```
## 4. Highest response ratio next(HRRN)

```python
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
            responseRatio = (
                currentTime - process.arrivalTime + process.burstTime
            ) / process.burstTime
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
        hrrnProcess.turnAroundTime = (
            hrrnProcess.completionTime - hrrnProcess.arrivalTime
        )
        hrrnProcess.waitTime = hrrnProcess.turnAroundTime - hrrnProcess.burstTime

        ratioQueue.enqueue(hrrnProcess)
        executionQueue.dequeue()

    executedProcesses = []
    while not ratioQueue.isEmpty():
        executedProcesses.append(ratioQueue.dequeue())

    executedProcesses.sort(key=lambda x: x.arrivalTime)
    return executedProcesses
```

# Usage
 
Using bash
```bash
git clone https://github.com/root39293/os-cpu-scheduling
cd os-cpu-scheduling
pip install matplotlib
```


# Screenshot

![image01](https://user-images.githubusercontent.com/72300594/236681670-35f19965-93d2-4dc1-ad88-81f5868fcb68.png)
![image02](https://user-images.githubusercontent.com/72300594/236681671-bd02a40a-7be2-4b00-a8a5-432a3f2e6808.png)
![image03](https://user-images.githubusercontent.com/72300594/236681672-1f43a93b-b0a2-4de9-8952-13facaf1a42b.png)
![image04](https://user-images.githubusercontent.com/72300594/236681674-c724d898-6a70-4b8e-8be4-493ed409a9ce.png)
