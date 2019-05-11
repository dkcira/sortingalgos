import random
import time
from copy import deepcopy
# the sorting algos
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort_wrapper
from heap_sort import heap_sort
from merge_sort import merge_sort_wrapper

array_length=300
original_array = [random.randint(-20, 60) for i in range(array_length)]

print(f'array length = {array_length}')
array = deepcopy(original_array)
bubble_sort(array)

array = deepcopy(original_array)
insertion_sort(array)

array = deepcopy(original_array)
quick_sort_wrapper(array)

array = deepcopy(original_array)
merge_sort_wrapper(array)

array = deepcopy(original_array)
heap_sort(array)