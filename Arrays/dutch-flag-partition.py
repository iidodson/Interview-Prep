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

print(dutch_flag_partition([3,2,9,7,1], 4))