from partition import partition

# low -> Starting element
# high -> Last element
def quicksort(arr,low,high):
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high)