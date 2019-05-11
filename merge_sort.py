from audit import audit

def merge_sort(array):
    """ merge sort """
    if len(array) > 1:
        mid = int(len(array) / 2)
        left = array[0:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        # merge
        l, r = 0, 0
        for i in range(len(array)):
            if (l < len(left)):
                lval = left[l]
            else:
                lval = None
            if ( r < len(right)):
                rval = right[r]
            else:
                rval = None
#            lval = left[l] if l < len(left) else None
#            rval = right[r] if r < len(right) else None
            if ((lval is not None) and (rval is not None) and lval < rval) or (rval is None):
                array[i] = lval
                l += 1
            elif ((lval is not None) and (rval is not None) and lval >= rval) or (lval is None):
                array[i] = rval
                r += 1
            else:
                raise Exception('cannot merge')
#            if( rval is not None or lval is not None):
#                if lval < rval or rval is None:
#                    array[i] = lval
#                    l += 1
#                elif lval >= rval or lval is None:
#                    array[i] = rval
#                    r +=1
#                else:
#                    raise Exception('cannot merge')
#        

@audit
def merge_sort_wrapper(array):
    """ avoid multiple measurements of audit due to recurrent calling """
    merge_sort(array)

if __name__ == '__main__':
    import random
    array = [random.randint(-20, 60) for i in range(32)]
    print(' array', array)
    merge_sort(array)
    print('sorted', array)