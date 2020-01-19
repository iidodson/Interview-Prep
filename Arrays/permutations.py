def __generateAllPermutations(runningCHoices, arr, allPermutations):
    if len(runningCHoices) == len(arr):
        allPermutations.append(runningCHoices)
        print(runningCHoices)
        return
       

    for i in range(len(arr)):
        choice = arr[i]
        if choice in runningCHoices:
            continue
        runningCHoices.append(choice)
        __generateAllPermutations(runningCHoices, arr, allPermutations)
        runningCHoices.pop()
    # [x**2 for x in range(6) if x%2 == 0

def permutatte(arr):
    allPermutations = []
    __generateAllPermutations([], arr, allPermutations)


print(permutatte("boat"))