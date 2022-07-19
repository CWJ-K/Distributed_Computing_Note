<!-- omit in toc -->
# Introduction
How to use more than one CPU at the same time to run codes in Python?

Using more CPUs increases **speed** for CPU-intensive problems and **responsiveness** for I/O-intensive code. 


<br />

<!-- omit in toc -->
# Table of Contents

<br />

# Fundamental Concepts

## Thread vs Processor
### Thread
* the smallest unit that operating systems can execute computation 
* a virtual version of a CPU core => one thread = one core
  * one CPU runs only one task/thread at any given point in time
  * in single CPU systems, multiple threads will not give true concurrency

<br />

### Processor
*

<br />

### Queue
* 
* 

<br />

## Multiple Threads
* Goal



<br />

## Multiple Processes
* Goal

<br />

## Multiprocess Queues
* Goal


<br />

# Packages
## threading
* Thread-based parallelism

<br />

## queue
* FIFO to perform tasks
* implements **multi-producer**, **multi-consumer** queues
  * useful in threaded programming when information must be exchanged safely **between multiple threads**
  * 

<br />

# Commands 
## threading


<br />

### thread_a.daemon
* a boolean value indicates whether thread_a is a daemon thread
  * **daemon thread**: a thread runs in the background
* should be set before `start()` is called

<br />

## queue
### queue_1.get()
* **remove** and **return** an item from the queue


<br />


### queue_1.task_done()
* indicate queue1 is finished
* [not for workers' benefits](https://stackoverflow.com/a/49637357), but `queue.join()`
  * let workers say they finish works 
  * `queue.join()` waits enough task_done calls have been made instead of checking the queue is empty

<br />

### queue_1.join()
* blocks queue_1 until all items in the queue_1 have been gotten and processed



# Reference

## TO DO
https://medium.com/omarelgabrys-blog/threads-vs-queues-a71e8dc30156