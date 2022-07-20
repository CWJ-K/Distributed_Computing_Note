<!-- omit in toc -->
# Table of Contents

<br />

# Introduction
Assume we use a multiprocessor/multicore system for exercises. 
<br />

# Structure
## Example1
* a program using multiple threads to download data from the Web to perform **I/O intensive computation**
* Insights
  * it is unknown whether threads run in the specific **orders**, which leads to **race condition** if actions depend on other actions performing in a given order
  * **race condition**
    * e.g. reference-counting algorithms: The counter goes to zero and the counter is increased by 1 at the different time. However, without giving the right order, the **segmentation fault** rises.
    * Solution: Locks
  * performing I/O intensive threads in parallel speeds the execution time
  
<br />

## Example2
* calculate Fibonacci to perform some **CPU-intensive computation**
* Insights:
  * the use of two threads takes twice as much time as one of a single thread => increases the execution time **linearly** because of **GIL**
  * Global Interpreter Lock (GIL):
    * **only one thread can be active** at any given time although Python threads are real OS-native threads
    * Jython does not have GIL
<br />

# Commands 

## Example1
```python
    python example_1.py EUR TWD USD
```

<br />

## Example2
```python
time python example_2.py -n 1 34

time python example_2.py -n 2 34

time python example_2.py -n 3 34

time python example_2.py -n 4 34

```