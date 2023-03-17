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

## factorial.py

The factorial() function takes an integer value x as its parameter and calculates its factorial using recursion. The base case for the recursion is when x equals 1, at which point the function simply returns 1. Otherwise, the function returns the product of x and the result of a recursive call to factorial(x-1).

To use this function, simply call it and pass in the integer value for which you want to calculate the factorial. For example, the line x = factorial(4) will calculate the factorial of 4 and store the result in the variable x.

Note that this implementation assumes that the input value x is a positive integer. If a non-integer or a negative integer is passed as input, the function may produce unexpected results. Therefore, it is recommended to perform appropriate input validation before using this function in a real-world scenario.

```vbnet
function fact(x)
    if x is equal to 1
        return 1
    else
        return x times fact(x minus 1)

set x to the result of calling fact with argument 4.
```