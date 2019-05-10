def quick_sort(array):
    """ quick sort """
    if len(array) > 1:
        pivot_index = int(len(array)/2)
        pivot_value = array[pivot_index]
        smaller = []
        larger  = []
        for i, val in enumerate(array):
            if i != pivot_index:
                if val < pivot_value:
                    smaller.append(val)
                else:
                    larger.append(val)
        quick_sort(smaller)
        quick_sort(larger)
        array[:] = smaller + [pivot_value] + larger


if __name__ == '__main__':
    import random
    array = [random.randint(-20, 60) for i in range(32)]
    print(' array', array)
    quick_sort(array)
    print('sorted', array)