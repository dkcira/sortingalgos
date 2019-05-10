def kth(array, k):
    pivot_point = len(array) / 2
    pivot_value = array[pivot_point]
    below = [s for s in array if s < pivot_value]
    above = [s for s in array if s > pivot_value]
    a = len(above)
    b = len(array) - len(below)
    if k < a:
        return kth(above, k)
    elif k > b:
        return kth(below, k-b)
    else:
        return pivot_value

import random
array = [random.randint(-100,100) for i in range(32)]
print("array", array)

k = 3
kval = kth(array, k)
print("k = ",k, " kval = ",kval)

from heap_sort import *
heap_sort(array)
print("sorted", array)
print(array[len(array) -k - 1])
