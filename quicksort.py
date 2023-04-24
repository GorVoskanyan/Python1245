'''
For manual testing run:
py quicksort.py
'''

from random import randrange
import doctest

def quick_sort(collection: list[int]) -> list[int]:
    '''Python implementation of quick sort algorithm.
    Examples:
    >>> quick_sort([])
    []
    >>> quick_sort([5])
    [5]
    >>> quick_sort([-5, 9, 2, 4, 8, -3])
    [-5, -3, 2, 4, 8, 9]
    '''

    if len(collection) < 2:
        return collection

    
    pivot_index = randrange(len(collection)) # use random element as pivot
    pivot = collection[pivot_index]
    greater: list = [] # all elements greater than pivot
    lesser: list = [] # all elemenst lesser than pivot 

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    # user_input = input('Enter numbers seperated by a comma: ')
    # unsorted = [int(item) for item in user_input.split(',')]
    # print(quick_sort(unsorted))
    # quick_sort([randrange(1000) for _ in range(1000)])
    doctest.testmod()
    print(quick_sort([-5, 9, 2, 4, 8, -3]))
