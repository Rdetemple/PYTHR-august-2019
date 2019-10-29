# Assignment: Conditionals - Part 1

In this homework, you will practice these programming concepts we've covered in class:

* Declaring and using variables
* Using mathematical operators
* Implementing conditionals: `if`, `elif`, and `else`

Part of this homework will be a mini-quiz and part will be code challenges.

## Deliverables

1. **Fork** the assignment repo
1. **Clone** your fork of the assignment repo onto your computer
1. Do your work inside your repo
1. **Commit** any new files that you create as well as any other changes
1. **Push** the changes to Github when you are done

## Submitting

To submit this assignment:

1. Go to the [assignment's main repo](https://git.generalassemb.ly/PYTHR-august-2019/hw-05-conditionals-part-1)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, fill in your name
1. In the comment field, paste the URL to your assignment repo
1. Click **Submit new issue** and you're done!

---

# Part 1: Mini-Quiz

The first part of this homework is a mini-quiz.

You can put all of your answers into a file called `part1.txt`.

1. True or false: An `if` statement can live without an `else` statement.

1. True or false: An `else` statement can live without an `if` statement.

1. True or false: An `elif` statement can live without an `if` statement.

1. True or false: An `if` + `elif` statement can live without an `else` statement.

1. True or false: The following statements are equivalent.

   ```python
   if a == True:
   ```

   ```python
   if a:
   ```

1. In the following code block, what prints?

   ```python
   a = True
   b = True
   c = False

   if a:
       print('1')

   if b:
       print('2')

   if c:
       print('3')

   if a and b:
       print('4')

   if a and c:
       print('5')

   if b and c:
       print('6')

   if a or b:
       print('7')

   if a or c:
       print('8')

   if b or c:
       print('9')
   ```

7. In the following code block, what prints?

   ```python
   a = False
   b = True
   c = True

   if a:
       print('1')
   elif b:
       print('2')
   elif c:
       print('3')
   else:
       print('4')
   ```

---

# Part 2: Most Clocks Are Normal, But Some Are Cuckoo!

## Skill you're Practicing: Writing Conditionals

For this problem, put your solution into a file called `part2.py`.

You're making a program for your coworkers that displays a message on their desktop's idle screen. Depending on the time of day, you want to print a different quote.

You'll create a variable, `time`, which has an integer value between zero and 23, representing the hour of the day in [military time](https://www.thebalancecareers.com/military-time-3356971), which is a 24-hour clock.

Write a conditional statement with Python code that prints exactly one message using the following rules:

* If the time of day is before 9 a.m. --> print the quote `'Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.'`

* Otherwise if the time of day is before or exactly 4 p.m. --> print the quote `'Working hard or hardly working?'`

* Otherwise, if the time of day is before 8 p.m. --> print the quote `'How did it get so late so soon?'`

* Otherwise if the time of day is before 10 p.m. --> print the quote `'A day without sunshine is like, you know, night.'`

* Otherwise, for any time 10 p.m. or later --> print the quote `'Burning the midnight oil!'`

## Starter Code

```python
time = 8

# Continue to write more code!
```

> **Hint:** Test your code with different values for time of day. Make sure you are only printing one statement, regardless of the value of `time`!

---

# Part 3: I Came, I 'Saur, I Conquered

## Skill you're Practicing: Writing Conditionals with Multiple Conditions

For this problem, put your solution into a file called `part3.py`.

The mighty Tyrannosaurus rex is the king of dinosaurs, and he does whatever he pleases. When he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he sleeps!

Write a conditional statement that selects one of the following actions for T-Rex based on his current mood. T-Rex's actions are ordered by precedence:

* If T-Rex is angry, hungry, and bored he will eat the Triceratops.
* Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
* Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
* Otherwise if T-Rex is tired, he goes to sleep.
* Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
* Otherwise if T-Rex is angry or bored, he roars.
* Otherwise T-Rex gives a toothy smile.

## Starter Code

```python
angry = True
bored = True
hungry = False
tired = False

# Example `if` statement:
if bored:
    print('T-Rex roars! RAWR!')
```

---

# All Done!

Now, go be like a T-Rex and do what you please!

![](https://media.giphy.com/media/1NFXnqVxzGr6w/giphy.gif)
