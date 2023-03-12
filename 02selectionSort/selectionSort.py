import numpy as np 
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

sample = np.random.randint(1, 100,size=(20)).tolist()
print(f"The ramdom generated list with the help of numpy: {sample}")
sortedList = selectionSort(sample)
print(f"The returned list from selectionSort function: {sortedList}")
