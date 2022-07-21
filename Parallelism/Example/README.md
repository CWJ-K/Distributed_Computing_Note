<!-- omit in toc -->
# Table of Contents

<br />

# Introduction
Assume we use a multiprocessor/multicore system for exercises. 
<br />

# Structure
## Example 1
* a program using multiple threads to download data from the Web to perform **I/O intensive computation**
* Insights
  * it is unknown whether threads run in the specific **orders**, which leads to **race condition** if actions depend on other actions performing in a given order
  * **race condition**
    * e.g. reference-counting algorithms: The counter goes to zero and the counter is increased by 1 at the different time. However, without giving the right order, the **segmentation fault** rises.
    * Solution: Locks
  * performing I/O intensive threads in parallel speeds the execution time
  
<br />

## Example 2
* calculate Fibonacci to perform some **CPU-intensive computation**
* Insights:
  * the use of two threads takes twice as much time as one of a single thread => increases the execution time **linearly** because of **GIL**
  * Global Interpreter Lock (GIL):
    * **only one thread can be active** at any given time although Python threads are real OS-native threads
    * Jython does not have GIL
  
<br />

## Example 3
* create a pool of worker processes to execute functions on each item of an input list
  * a process with a thread uses a CPU core
  * e.g. 4 worker processes using 4 CPU cores execute the same 4 functions in parallel (TBC)

<br />

## Example 4
* same as Example 3, but without a context manager

<br />

## Example 5
* same as Example 3, but using multiple threads
* performance is the same as Example 2

<br />

## Example 6
* execute functions by multiprocess queues
* two-queue architecture
  * one queue: hold tasks to be performed
  * one queue: hold results
  * `task.put(None)` to signal that the worker process should quit
* performance is the same as Example 3

<br />

# Commands 

## Example 1
```python
    python example_1.py EUR TWD USD
```

<br />

## Example 2
```python
time python example_2.py -n 1 34

time python example_2.py -n 2 34

time python example_2.py -n 3 34

time python example_2.py -n 4 34

```

<br />

## Example 3
```s
  time python example_3.py -n 1
  time python example_3.py -n 2
  time python example_3.py -n 3
  time python example_3.py -n 4

  # over the number of cores leads to a linear increase in execution time
  time python example_3.py -n 8
  time python example_3.py -n 16

```

<br />

## Example 5

```python 
  time python example_5.py -n 1
  time python example_5.py -n 2
  time python example_5.py -n 3

```