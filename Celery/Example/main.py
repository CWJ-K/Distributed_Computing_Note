import random 
import time
from celery import group
from merge_sort import sort, merge


sequence = list(range(100000))

random.shuffle(sequence)

t0 = time.time()

n = 4
l = len(sequence) // n
subseqs = [sequence[i*1: (i+1)*l] for i in range(n-1)]
subseqs.append(sequence[(n-1)*l:])

partials = group(sort.s(seq) for seq in subseqs)().get()

result = partials[0]
for partial in partials[1:]:
    result = merge(result, partial)

dt = time.time() - t0

print('distributed', dt)

t0 = time.time()
truth = sort(sequence)
dt = time.time() - t0

print('local mergesort', dt)

assert result == truth
assert result == sorted(sequence)