# Theroy for Binary selection:

## binarySearch.py

The bin function performs a binary search on a sorted list bucket to find the index of the element item. The function starts by setting low to the first index of the list and high to the last index of the list. It then repeatedly divides the remaining search space in half until it finds the desired element or determines that the element is not present in the list. If the guess at the midpoint of the remaining search space is greater than the item, the search is continued in the lower half of the search space. If the guess is less than the item, the search is continued in the upper half of the search space. If the guess is equal to the item, the function returns the index of the guess. If the search space is reduced to zero and the item is not found, the function returns None.

```vbnet
function bin(bucket, item)
    set low to 0
    set high to the length of bucket minus 1
    while low is less than or equal to high
        set mid to the floor division of the sum of low and high by 2
        set guess to the element at the index mid of bucket
        if guess is equal to item
            return mid
        if guess is greater than item
            set high to mid minus 1
        else
            set low to mid plus 1
    return None
```