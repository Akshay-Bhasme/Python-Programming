from array import *
def max_val(arr):
    min = 0
    for j in range(len(arr)):
        if arr[j] < min:
            min = arr[j]
        else:
            min = min

    max=min
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        else:
            max = max
    return max

def min_val(max):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        else:
            max = max

    min=max
    for j in range(len(arr)):
        if arr[j]< min:
            min= arr[j]
        else:
            min= min

    return min

arr = array('i', [1,-2, -5, -4, -3,-15,20,-19])
k= max_val(arr)
print('Maximum value from array is: ',k)
l= min_val(arr)
print('Minimum value from array is: ',l)