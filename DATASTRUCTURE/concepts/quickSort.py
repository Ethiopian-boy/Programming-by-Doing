"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, low, high):
     if low < high:
        pi = partion(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

def partion(array, low, high):
    # choose the pivot element
    pivot = array[high]
    # pointer to the larger element
    i = low - 1
    # traverse and compare through all elements
    for j in range(low, high):
        # If element smaller than pivot is found
        # swap it with the greater element pointed by i
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    # swap the greater element with pivot
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test, 0, len(test) - 1)
print(test)

 