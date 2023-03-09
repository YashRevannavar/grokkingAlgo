def bin(bucket,item):
    low = 0
    high = len(bucket)-1
    while low <= high:
        mid = (low+high)//2 
        guess = bucket[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

bucket = [1,2,3,4,5,6,7,8,9]
solution = bin(bucket=bucket,item=3)
print(solution)
