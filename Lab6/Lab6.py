def quick_sort(arr, start, end):
#TODO: Implement this recursive quick sort method. 
# This method 	should also print  the array segment (between start and end index) 	before partitioning, the pivot, 
# and the segment after partitioning
    if start < end:
        # Print the header for this sorting step
        print(f"------ Quick sorting from index: {start} to {end} -----")

        # Print the array segment before partitioning
        print("Array segment before partitioning:", " ".join(map(str, arr[start:end+1])))

        # Partition the array and get the pivot index
        pivot_index = partition(arr, start, end)

        # Print the pivot
        print("Pivot:", arr[pivot_index])

        # Print the array segment after partitioning
        print("Array segment after partitioning:", " ".join(map(str, arr[start:end+1])))

        # Recursively sort the subarrays on either side of the pivot
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, low, high):
#TODO: Implement this method. 
# This method should partition the 	array segment (between low and high) based on the pivot.
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i+1] (position of the pivot) and arr[high]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index of the pivot element
    return i + 1

# Test the quicksort algorithm
arr = [11, 12, 1, 9, 6, 5, 4, 7]
quick_sort(arr, 0, len(arr) - 1)
print('The final sorted array:', arr)