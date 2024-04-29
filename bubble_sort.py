from audit import audit

@audit
def bubble_sort(array):
    """ bubble sort """
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

@audit
def bubble_sort2(array):
    """ bubble sort """
    for i in range(len(array)):
        for j in range(len(array)-1 -i):
            if array[i] < array[j]:
                array[i],array[j] = array[j],array[i]


if __name__ == '__main__':
    import random
    array = [random.randint(-20, 60) for i in range(32)]
    print(' array', array)
    bubble_sort(array)
    print('sorted', array)
