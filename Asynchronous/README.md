<!-- omit in toc -->
# Introduction
How to program in asynchronous?
<br />

<!-- omit in toc -->
# Table of Contents
- [Fundamental Concepts](#fundamental-concepts)
  - [Execution process Without Asynchronous](#execution-process-without-asynchronous)
  - [Asynchronous (event-driven)](#asynchronous-event-driven)
  - [Iterators](#iterators)
    - [Iteration Protocol](#iteration-protocol)
  - [Generator](#generator)
  - [Coroutines](#coroutines)
- [Commands](#commands)
  - [Iterator](#iterator)
  - [generator](#generator-1)
  - [coroutine](#coroutine)

<br />

# Fundamental Concepts
## Execution process Without Asynchronous
* each task performs its I/O operations and waits to start until the previous task is finished
* in the process of each task, there are idle CPUs because of waiting data 


## Asynchronous (event-driven)
* Advantage - release idle CPUs to other tasks
  * when one task is waiting on I/O (the task is blocking), which is suspended at the time and there are idle CPUs, the task voluntarily gives up the memory to another task
  * benefits more on **I/O-intensive tasks** rather than CPU-intensive tasks
    * e.g. disk access, network communication
* still executes only one task at any given time
  * but can be mixed with multi-thread Programs or others

* different from multi-thread program
  |Type|How|
  |:---:|:---|
  |Multi-thread Program|the operating system decides which threads are active and when they are suspended|
  |Asynchronous|tasks decide when to give up the CPU and therefore suspend their execution|

<br />

## Iterators
* objects can be iterated because the **iteration protocol**
  > not because they are lists or strings

<br />

### Iteration Protocol
* defines a standard interface for iteration
  * an object implementing `__iter__` and `__next__` in Python
  * `__iter__`: return the object to be iterated
  * `__next__`: return the single element of the sequence one by one

<br />

## Generator
* a **callable** that **generates** a sequence of results rather than returning a result
* uses `yielding` to yield the individual value instead to return it
  * calling the generator function does not generate the sequence, but only a **generator object**
  * uses `next` to get a value from the generated sequence until the sequence is empty
* a simple way to write iterators without `__iter__` and `__next__`

<br />

## Coroutines
* enables to **resume and suspend** the execution of a **function** midway
  > via `yield`
* should understand `generators` and `iterators` first
* not conceptually generators, reasons are:
  1. coroutines are not associated with iteration
    > only use the concepts of generators (TBC)
  2. generators produce values, but coroutines **consume** values
* Structure of coroutines
    |Component|Meaning|
    |:---:|:---|
    |`yield()`|suspend the execution of the coroutine|
    |`send()`|pass data to coroutine and hence resume its execution|
    |`close()`|terminate a coroutine. The only way to exit the loop|
* applications: sending data to multiple coroutines and getting data from multiple resources => network programming, system programming, reimplement Unix tools in Python

<br />


# Commands

## Iterator

```python
  class MyIterator(object):
    def __init__(self, xs):
      self.xs = xs
    
    def __iter__(self):
      return self
    
    def __next__(self):
      if self.xs:
        return self.xs.pop(0)
  
      else:
        raise StopIteration
  
  iter.__iter__()

  iter.__next__()

  next(iter)

```

* once the sequence is exhausted, next() throws a StopIteration exception
* `for loop` uses the same mechanism


## generator
```python

    def mygenerator(n):
        while n:
            n -= 1
            yield n

    a = mygenerator(5)

    next(a)
    a.__iter__()
    a.__next__()


```

## coroutine
```python
    def complain_about(content):
        print('Please talk to me!')
        
        try:
            while True:
                text = (yield)
                if content in text:
                    print(f'On no! I found {content} again')
        except GeneratorExit:
            print('Ok, ok, I am quitting')
    

    c = complain_about('wine')
    c
    next(c)
    c.send('Give me more wine!')
    c.close()
```

```python
# without exception
def complain_about(content):
    print('Please talk to me!')
    
    while True:
        text = (yield)
        if content in text:
            print(f'On no! I found {content} again')

```

```python
# without calling next()
def coroutine(fn):
    def wrapper(*args, **kwargs):
        c = fn(*args, **kwargs)
        next(c)
        return c
    return wrapper


@coroutine
def complain_about(content):
    print('Please talk to me!')
    
    try:
        while True:
            text = (yield)
            if content in text:
                print(f'On no! I found {content} again')
    except GeneratorExit:
        print('Ok, ok, I am quitting')

```


* call `next()` to use coroutine
  > like calling a generator


* without `try...except`, the coroutine will simply stop working, `StopIteration`, instead of returning the exception, `GeneratorExit`


* annoying `next()` can be wrapped, so coroutine can be directly used without calling `next()` first
