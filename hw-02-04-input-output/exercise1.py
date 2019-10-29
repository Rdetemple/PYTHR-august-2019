
# Exercise 1 # QUESTION: 1
tip = .20
meal_cost = 55
total = tip * meal_cost
print(total)

# Exercise 1 # QUESTION: 2
tip = .20
meal_cost = 55
total = tip * meal_cost
print('$', total)

# Exercise 1 # QUESTION: 3
x = 45628
y = 7839
total = x * y
print("The Results of the mutilplication is", total)

# Exercise 1 # QUESTION: 4
#string = 'word'
#int = 1
#total = string + int
#print(total)
#TypeError: can only concatenate str (not "int") to str
string = 'word'
number = 1
total = string + str(number)
print(total)

# Exercise 2 # QUESTION: 1
print('What is your name?')
user_name = input()
print(f'Hello, {user_name}')
print('How old are you?')
user_age = input()
year = 2019
total = year - int(user_age)
print(f'You were born in the year', total)
