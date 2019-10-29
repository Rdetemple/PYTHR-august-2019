# Assignment: Programming Fundamentals - Input and Output

The next few assignments is about walking you through the fundamental features of the Python language using short, simplified code examples.

If you find yourself wondering "why would I ever write this code?" or "ok, but what is this thing _for_?", try not to panic! Today's assignment is about discovering **what** is possible in Python, not **why** those features are useful.

However, if you can start to envision how you might use these features in more complicated programming scenarios, that's great!

## Learning Goals

* Creating local `.py` files and adding them to a repo
* Understanding Basic Data Types
* Converting between Basic Data Types
* Input and Output with `input` and `print`

---

# Assignment

## Exercise 1

Create a new file called `exercise1.py`. Open it up in your text editor and enter the solutions for the problems below.

Try annotating your code by leaving comments (using the `#` symbol) in the file, before each of your answers to the following questions.

Be sure to **commit** after answering each question!

1. How would you calculate a good tip for a 55 dollar meal? Use `print` to print the numerical tip you would give.
    > Example Output: `8.25`

1. Now, print the tip with a `$` in front of it. You'll have to do **type conversion** to make this work.
    > Example Output: `$8.25`

1. Try outputting the result of 45628 multiplied by 7839, in a sentence. You will have to use string **interpolation**.
    > Example Output: `The result of the mutiplication is XXXXXXXX`

1. Try adding a **string** and an **integer** together with the `+` operator. What happens? Find a way to convert the integer into a string before adding them together, and use `print` to print the result.

1. (**STRETCH**) What's the value of the expression `(10 < 20 and 30 < 20) or not (10 == 11)`? Try figuring it out on your own before typing it in. (This is a hard one, don't worry if you can't get it, but please try!)

## Exercise 2

Let's make a Python program that greets someone by name. Create a new file called `exercise2.py` and open it up in your code editor.

Start with displaying a question:

```python
print('What is your name?')
```
Run your program to verify that it works so far. If it works, commit what you've got to git with a meaningful commit message.

The next step is to get input from your hypothetical user (which for now is just you).

We can do that with `input()`. `input()` will pause the execution of your program and give your user the chance to type something into their terminal.  When the user finishes typing and hits "enter", the value that they typed in is **returned** by `input()` and your program resumes normal execution.

Try assigning `input()` to a variable in order to save your user's input.

```python
print('What is your name?')
user_name = input()
print(f'Hello, {user_name}')
```

Note that `input()` always *gives back the user's input in a string*.

Having that input string stored in a variable allows us to display it back to the user later on.

### Your Challenge

Ask the user how old they are, and have the program output what year **they were born in**.

For example, if the user enters `19`, the output should be something like `You were born in the year 2000`.

Don't forget to commit your work again!

## Exercise 3

This exercise will give you a quick exposure to booleans. We'll explain booleans in more detail later in the course, but for now we would like you to get a small bit of practice with them so that they'll make more sense later.

Try the following examples for yourself in the Python shell. *There is no need to submit the results of Exercise 3*, it's purely for your enjoyment.

```python
True and True
# --> True
not True
# --> False
not False
# --> True
True and False
# --> False
True and not False
# --> True
True or False
# --> True
True or True
# --> True
False or True
# --> True
False or False
# --> False
not False or False
# --> True
```

You can also try combining comparison and logical operators like so:

```python
(1 < 3) and (3 < 5)
# --> True

(1 > 1) and (2 > 2)
# --> False

(1 == 2) or (2 < 3)
# --> True

(1 != 2) or (2 < 3)
# --> True

(1 == 2) or (2 == 3)
# --> False
```

The purpose of boolean logic will become clearer later on when we talk about **control structures**. For now, let's put booleans in your back pocket.

---

# Deliverables

1. **Fork** the assignment repo.

1. Open your Terminal and navigate to the folder for all of your development work.

1. **Clone** your copy of the assignment repo onto your computer. Remember to clone *your* version of the repo, not the instructor's version, so that you can make change to it!

1. Open the assignment folder with your code editor.

1. Put your solution code inside your repo.

1. Be sure to **commit** any new files that you create as well as any other changes.

1. When you're done, **push** the changes to Github.

---

# Submitting

To submit this assignment:

1. Go to the [assignment's main repo](https://git.generalassemb.ly/PYTHR-august-2019/hw-02-04-input-output)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, fill in your name
1. In the comment field, copy and paste the URL to your assignment repo
1. Click **Submit new issue** and you're done!
