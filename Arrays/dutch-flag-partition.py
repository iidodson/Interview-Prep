def dutch_flag_partition(arr, pivot):
    pivotNumber = arr[pivot]
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[j] < pivotNumber:
                arr[i], arr[j] = arr[j], arr[i]
                break

    for k in reversed(range(len(arr))):
        if arr[k] < pivotNumber:
            break
        for l in reversed(range(k)):
            if arr[l] > pivotNumber:
                arr[k], arr[l] = arr[l], arr[k]
                break
    return arr

# print(dutch_flag_partition([3,2,9,7,1], 4))

def dutch_flag_partition_V2(arr, pivot):
    current = 0
    large = len(arr) - 1
    pivot = arr[pivot]
    small = 0
    # Watch out for the end case where th4 values may be equal
    while current < large: 
        if arr[current] < pivot:
            arr[current], arr[small] = arr[small], arr[current]
            current += 1
            small += 1
        elif arr[current] > pivot:
             arr[current], arr[large] = arr[large], arr[current]
             large -= 1
        elif current == pivot:
            current += 1
    return arr
print(dutch_flag_partition_V2([9,2,1,7], 1))
    