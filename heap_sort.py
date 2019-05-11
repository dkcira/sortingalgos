import heapq
from audit import audit

@audit
def heap_sort(array):
    """ heap sort """
    heapq.heapify(array)
    array[:] = [heapq.heappop(array) for i in range(len(array))]


if __name__ == '__main__':
    import random
    array = [random.randint(-20, 60) for i in range(32)]
    print(' array', array)
    heap_sort(array)
    print('sorted', array)