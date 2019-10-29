# Exercise 1
# Write a FUNction called double that accepts an argument called my_number and
# returns that number multiplied by 2.
#
# Try calling it multiple times and pass in different numbers each time.

def double (my_number):
    cal = my_number * 2
    print(f'The new calculation is', cal)

double(2)
double(3)

#--------------------------
# Exercise 2
# Write a FUNction called negative that accepts a number as an argument and
# returns a boolean (true/false)
# indicating whether that number is negative or not.
# Try calling it multiple times, passing in different numbers each time.
# What should the FUNction return if the number is exactly 0? (Hint: 0 is not
# a negative number)

def negative (my_number2):
    bool(my_number2)
    print(bool(my_number2))

negative(-1)
negative(2)
negative(3)

#--------------------------
# Exercise 3
# Write a FUNction that accepts a string as an argument and returns False if
# the word is less than 8 characters long. (This time, you make up a name for the FUNction!)
# What should the FUNction return if the word is longer than 8 characters long?
# What should the FUNction return if the word is exactly 8 characters long?

def letter_Counter (input):
    if len(input) < 8:
        print (False)
    else:
        return True

letter_Counter("d")
