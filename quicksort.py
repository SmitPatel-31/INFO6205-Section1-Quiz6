def quicksort(arr, low=0, high=None):
    """
    Implementation of quicksort algorithm.
    
    Args:
        arr: List to be sorted
        low: Starting index of the array
        high: Ending index of the array
        
    Returns:
        Sorted list
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)  # Sort left part
        quicksort(arr, pivot_index + 1, high)  # Sort right part
    
    return arr


def partition(arr, low, high):
    """
    Partition the array and return the pivot index.
    
    Args:
        arr: List to be partitioned
        low: Starting index of the segment
        high: Ending index of the segment
        
    Returns:
        The position of the pivot after partitioning
    """
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)  # Swap elements to move smaller elements to the left

    swap(arr, i + 1, high)  # Swap pivot element to its correct position
    return i + 1


def swap(arr, i, j):
    """
    Helper function to swap two elements in an array.
    
    Args:
        arr: List containing elements to swap
        i: Index of first element
        j: Index of second element
    """
    arr[i], arr[j] = arr[j], arr[i]


def is_sorted(arr):
    """
    Helper function to check if an array is sorted.
    
    Args:
        arr: List to check
        
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
