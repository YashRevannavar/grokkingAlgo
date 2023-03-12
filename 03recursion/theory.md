# Theroy for Recursion

## countDown.py

The provided code is a Python program that defines a function called countDown which takes an integer argument i as input. The purpose of this function is to print a countdown from i down to 1, with a delay of 1 second between each count.

The countDown function first prints the current value of i to the console, using the print function and an f-string to format the output string. It then uses the sleep function from the time module to pause the program for 1 second.

Next, the function checks if the value of i is less than or equal to 0. If so, it returns from the function, effectively ending the countdown. If i is greater than 0, the function recursively calls itself with the argument i-1, continuing the countdown until it reaches 0.

Finally, the countDown function is called with an initial value of 10 to start the countdown. When the program is run, the countdown will be printed to the console, with each number displayed for 1 second before the next one is printed.

```vbnet
function countDown(i)
    display "The value of i : " concatenated with the value of i and a new line character
    pause the program for 1 second using sleep functio from time module
        if i is less than or equal to 0
        return
    else
        call the function countDown with argument i-1
    end if
end function
```