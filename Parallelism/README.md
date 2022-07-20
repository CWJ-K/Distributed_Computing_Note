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
* Improve performance of **I/O intensive threads**
  * Issue: race condition
  * Solution: Lock
* No effects on **CPU-intensive computation** because of GLI

<br />

### Packages
* threading
  * Thread-based parallelism
* queue
  * FIFO to perform tasks
  * implements **multi-producer**, **multi-consumer** queues
    * useful in threaded programming when information must be exchanged safely **between multiple threads**

<br />

## Multiple Processes
* process-based parallelism
* Improve performance of CPU-intensive computation
  * use multiple processes instead of multiple threads to work around the GIL
* Disadvantage
  * launching multiple instances of Python interpreter spends startup time and memory usage
* Advantage
  * multiple processes have their memory => **share-nothing architecture**
  * easily scale to a distributed application from a single-machine

<br />

### Packages
* multiprocessing
* concurrent.futures
  * builds on top of multiprocessing

<br />

## Multiprocess Queues
* Goal


  

<br />

# Commands 
## threading
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

### queue.join()
* blocks queue until all items in the queue have been gotten and processed
  * until enough task_done calls are received, the system starts to do other things

<br />

### concurrent.futures




<br />


# Reference

## TO DO
https://medium.com/omarelgabrys-blog/threads-vs-queues-a71e8dc30156