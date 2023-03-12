from time import sleep
def countDown(i):
    print(f"The value of i : {i}\n")
    sleep(1)
    if i <= 0:
        return
    else:
        countDown(i-1)

countDown(10)