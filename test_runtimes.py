import random
import time
from copy import deepcopy
from bubble_sort import bubble_sort

original_array = [random.randint(-20, 60) for i in range(32)]

array = deepcopy(original_array)
bubble_sort(array)