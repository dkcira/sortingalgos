def quick_sort(array):
    """ quick sort """
    if len(array) > 1:
        pivot_point = int(len(array) / 2)
        pivot_value = array[pivot_point]
        below = [s for s in array if s < pivot_value]
        above = [s for s in array if s > pivot_value]
        quick_sort(below)
        quick_sort(above)
        array[:] = below + [pivot_value] + above


if __name__ == '__main__':
    import random
    array = [random.randint(-20, 60) for i in range(32)]
    print(' array', array)
    quick_sort(array)
    print('sorted', array)