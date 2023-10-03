def merge_sort(arr,left,right):
    if left < right:
       # calculate the midpoint of the array
        mid = (left + right) // 2
       # recursively sort the left and right halves of the array
        merge_sort(arr, left,mid)
        merge_sort(arr, mid+1,right)
        # Merge the sorted halves. 
        merge(arr,left,mid,right)
def merge(arr,left,mid,right):
    # calculate the size of the merged array.

    merged_size = right - left + 1
    merged = [0]*merged_size
    i = left
    j = mid+1
    k = 0
    # merge the two halves while keeping descending order
    while i <= mid and j <= right:
        # Reverses the function in descending order
        if arr[i] >= arr[j]:
            merged[k] = arr[i]
            i += 1
        else:
            merged[k] = arr[j]
            j += 1
        k += 1
    
    # SORT any remaining elements in the left half
    while i <= mid:
        merged[k] = arr[i]
        i += 1
        k += 1
    # SORT any remaining elements in the right half

    while j <= right:
        merged[k] = arr[j]
        j += 1
        k += 1
# Copy the merged elements back into the original array
    k = 0
    while k < merged_size:
        arr[left + k] = merged[k]
        k += 1
nums = [11,12,1,9,6,5,4,7]
merge_sort(nums,0, len(nums)-1)
#prints the sorted list
for num in nums:
    print(num, end=' ')