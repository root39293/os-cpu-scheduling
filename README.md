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

# Implementation

In this project, we will implement several CPU scheduling techniques and analyze the test results. We will use Python to implement the program and analyze the results.

The scheduling algorithms I have chosen are


## 1. FCFS (First-Come First-Served)
```python
def FCFS(processes):
    readyQueue = Queue()
    for process in processes:
        readyQueue.enqueue(process)

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
## 2. Shortest Job first (Non-preemptive)

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
## 4. Priority Scheduling