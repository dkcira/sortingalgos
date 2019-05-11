from audit import audit

@audit
def insertion_sort(array):
    """ insertion sort """
    for i in range(len(array)):
        j = i
        # push as much to the left as possible
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


if __name__ == '__main__':
    import random
    array = [random.randint(-20, 60) for i in range(32)]
    print(' array', array)
    insertion_sort(array)
    print('sorted', array)