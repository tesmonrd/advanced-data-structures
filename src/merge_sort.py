import random


def mergesort(in_list):
    """Implement merge sort."""
    if len(in_list) > 1:
        mid = len(in_list) // 2
        left = mergesort(in_list[:mid])
        right = mergesort(in_list[mid:])
        return(merge(left, right))
    else:
        return in_list


def merge(left, right):
    """Make the sorted merge list."""
    new = []
    lidx = 0
    ridx = 0
    while lidx < len(left) and ridx < len(right):
        if left[lidx] < right[ridx]:
            new.append(left[lidx])
            lidx += 1
        elif right[ridx] < left[lidx]:
            new.append(right[ridx])
            ridx += 1
        else:
            new.append(left[lidx])
            new.append(right[ridx])
            lidx += 1
            ridx += 1
    if lidx < len(left):
        new.extend(left[lidx:])
    elif ridx < len(right):
        new.extend(right[ridx:])
    return new


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit
    LIST_ONE = [2, 1, 4, 3]
    LIST_TWO = [random.randint(0, 1000000) for i in range(10000)]
    print("Merge Sort")
    print("Divides unsorted list into n sublists,\
 and repeatedly sorts and merges sublists into one sorted list.")
    print("It's stable and most efficient on small lists.")
    print("Input: [2, 1, 4, 3], Runs: 500")
    wrapped = wrapper(mergesort, LIST_ONE)
    print('Total time: ', timeit.timeit(wrapped, number=500))
    print("Input: [random.randint(0, 1000000) for i in range(10000)], Runs: 500")
    wrapped = wrapper(mergesort, LIST_TWO)
    print('Total time: ', timeit.timeit(wrapped, number=500))
