# Theroy for Selection sort:

## selectionSort.py

The findSmallest function finds the index of the smallest element in an input list by iterating over the list and comparing each element with the current smallest element. It returns the index of the smallest element.

The selectionSort function sorts the input list by repeatedly finding the smallest element in the remaining unsorted part of the list and moving it to the end of a new list. The sorted list is then returned.

```vbnet
function findSmallest(arr)
    set the variable smallest as the first element in arr
    set the variable smallestIndex to 0
    for each element i in arr starting from the second element
        if i is smaller than smallest
            set smallest to i
            set smallestIndex to the index of i
    return smallestIndex

function selectionSort(arr)
    create an empty list newArr
    for each element i in arr
        find the index of the smallest element in arr using findSmallest function
        remove the smallest element from arr and append it to newArr
    return newArr

```