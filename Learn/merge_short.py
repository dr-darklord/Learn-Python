
        
def merge(left, right):
    merged = []
    i = j = 0
    
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add the remaining elements from left and right arrays
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array
    mid = len(arr) // 2
    
    # Recursively divide the array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the two sorted halves
    return merge(left, right)

# Example usage
arr = [38, 22, 55, 66, 77, 88, 12, 1, 2, 5]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
