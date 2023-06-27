from functools import wraps
import time


#  Simple decorator to measure execution time
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def shell_sort(array: list) -> None:
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    print(f"Shellsort: {array}")


#  Quick sort
#  function to find the partition position
def partition(array, low, high):
    #  choose the rightmost element as pivot
    pivot = array[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quick_sort(array: list, low, high) -> None:
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
        # recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


#  Used to measuring time for recursion
@timeit
def timed_quicksort(array: list, low, high):
    quick_sort(array, low, high)
    print(f"Quicksort: {array}")


# Bubble sort
@timeit
def bubble_sort(array):
    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(f"Bubble sort: {array}")


# Driver code to test above
arr = [9, 23, 701, 4, 301, 88, 57, 28, 10, 1]
shell_sort(arr)
arr = [9, 23, 701, 4, 301, 88, 57, 28, 10, 1]
timed_quicksort(arr, 0, len(arr) - 1)
arr = [9, 23, 701, 4, 301, 88, 57, 28, 10, 1]
bubble_sort(arr)
