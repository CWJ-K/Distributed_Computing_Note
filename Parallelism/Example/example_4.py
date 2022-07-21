import concurrent.futures as cf

def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise Exception('fib(n) is undefined for n < 0')
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':

    pool = cf.ProcessPoolExecutor(max_workers=1)
    future = pool.submit(fib, 34)
    print('pool', pool, 'future', future)

    future.running()
    future.done()

    # test timeout
    #future.result(timeout=0)
    
    future.result(timeout=None)
    print('finished future', future)
    
    print('done', future.done())

    print('running', future.running())

    print('cancel', future.cancelled())

    print('exception', future.exception())