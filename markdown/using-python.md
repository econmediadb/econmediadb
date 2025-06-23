# Using Python



## Python series (on linux.org)

1. [Installing and Configuring Python 3](https://linux.org/threads/python-series-part-1-installing-and-configuring-python-3.48009/)
2. [Python Basics ](https://linux.org/threads/python-series-part-2-python-basics.48363/)
3. [Python Operators ](https://linux.org/threads/python-series-part-3-python-operators.48827/)
4. [Flow Control ](https://linux.org/threads/python-series-part-4-flow-control.49172/)
5. [Functions ](https://linux.org/threads/python-series-part-5-functions.49670/)
6. [Printing Strings](https://linux.org/threads/python-series-part-6-printing-strings.50093/)
7. [User Input ](https://linux.org/threads/python-series-part-7-user-input.50605/)
8. [Data Structures](https://linux.org/threads/python-series-part-8-data-structures.51110/)
9. [File I/O](https://linux.org/threads/python-series-part-9-file-i-o.51469/)
10. [Error Management](https://linux.org/threads/python-series-part-10-error-management.52961/)
11. [Classes](https://linux.org/threads/python-series-part-11-classes.53539/)
12. [Example Game](https://www.linux.org/threads/python-series-part-12-example-game.54116/)
13. [Starting with Tkinter](https://www.linux.org/threads/python-series-part-13-starting-with-tkinter.55094/)
14. [Understanding Pack in Tkinter](https://www.linux.org/threads/python-series-part-14-understanding-pack-in-tkinter.55552/)
15. [Mastering Widget Placement with Tkinter’s place Method](https://www.linux.org/threads/python-series-part-15-mastering-widget-placement-with-tkinter%E2%80%99s-place-method.56041/)


### 1. Installing and Configuring Python 3

If I should look at https://python.org/downloads, I can see that there is a release for Python 12. You could download the source code and install it, but the version in the repository should be a very stable version.

### 2. Python Basics

#### Keywords

Keywords are actual words that are used for commands, sometimes these are called identifiers. 

Some words are keywords, but not a command. These words would be something like 'else' or 'elif' that goes with the 'if' keyword.

#### Variables

Variables are used to represent other characters or numbers. Algebra is a great example. When 'x=2' and 'y=5'. These are variables.

Variables can also be 'strings' of characters, such as 'c=Linux'. Or even a combination of letters and numbers.

#### Variable Data Types

We can see the data type of variable by printing out the command 'type(variable)'. So, if we had a variable 'a' and we wanted to know the data type, the command is 'print (type(a))'.


    f=3.14159
    print ("Float ", type(f))
    i=1
    print ("Integer ", type(i))
    c=1+3j
    print ("Complex ", type(c))
    s="Linux"
    print ("String ", type(s))
    b=True
    print ("Boolean ", type(b))
    l=["Linux", "Windows", "macOS"]
    print ("List ", type(l))


The output is:

    Float <class 'float'>
    Integer <class 'int'>
    Complex <class 'complex'>
    String <class 'str'>
    Boolean <class 'bool'>
    List <class 'list'>

The 'float' data type has a decimal. The 'integer' is a whole number. 'Complex' numbers contain a real number, '1', and an imaginary number, '3j'. A 'string' is text. The 'boolean' type is 'True' or 'False', and it has to start with a capital letter. Another data type listed is 'list', which is assigned with brackets. You can think of the List data type as similar to an array. We can get into those in a later article.

After setting a variable as a data type, you can just assign it a new value and it should change to that data type. For example, if I assign the variable 'b' a value of '1', it is of type 'integer'. Then if I assign it the value of 'Linux', the type is now a 'string'.

If you perform arithmetic operations to the variable, you can change the data type. An example would be that we assign a value of '1'. The variable is an integer. We then use the operation of multiplying the variable times '1.1' in the line 'a=(a*1.1)'. This takes the value in 'a' and multiplies it by '1.1' and then reassigns it back to the variable 'a'. The variable is now of a data type 'float'. If we should perform another mathematical operation to undo the changes, divide by '1.1', the new value is '1.0' and it is still the data type float.

#### Input Data

So far, we have assigned values to variables in the coding. What if we would want to ask the user for information?

We can use the 'input' command to get data from the user.

Let's try something basic, such as asking for the name. The variable ‘name’ receives the data. We would then print the name with the data type. The code would be:

    name=input("What is your first name? ")
    print ("Hello ", name)
    print (name, "is of data type: ", type(name))

The 'input' command uses the prompt for the user, 'What is your first name? '. The variable ‘name’ receives the string entered.

Notice, I said 'the string' entered is placed into a variable. Anything you type, even if you enter an integer, would be of data type 'string'. We can reassign data types, but again, this is for another article.

After you run the code, click at the bottom, which is a 'terminal' where the programs run. Type in your name when prompted and see the results.


### 3. Python Operators

#### 3.1. Arithmetic Operations

As with other programming languages, we can perform basic math functions. Such as:

Addition +

Subtraction -

Multiplication *

Division /

Exponent **

Modulus %

Keep in mind that the values we are performing these operations on can be a variable or an actual number. For example, if we wanted to add 2 and 3, we could use the numbers and print out the answer:

    print (2+3)

If we wanted to use variables, we can do:

    a=2
    b=3
    print (a+b)

It is possible to mix numbers and variables:

    a=2
    print (a+3)

These are fairly straightforward, but let's look at the last two arithmetic operators.

Exponents is when a number has a power. For example, 2 to the third power, 2**3, is two times two times two, or eight.

Modulus is the remainder of a division operation. For example:

    a=10
    b=3
    print (a/b)
    print (a%b)

The first output is:

    3.3333333333333335
    1

The first line of output is 10 divided by 3. The second line is the remainder of 10 divided by 3. If we divide 10 by 3, we get 3 with a remainder of 1, so the answer is 1.


#### 3.2. Arithmetic Assignments

In a lot of cases, you may perform calculations on a variable. Instead of storing the new value in a new variable, you can use the same variable. The difference is that you can use a shorthand way of performing the calculation called an assignment.

So, if we have a game that we are tracking the number of levels that a player reaches, we could do:

    level = (level +1)

The code can be run every time the player levels up.

The benefit of placing the value back into the existing variable and not a new one is so you don't have a lot of variables to track, but also every variable requires more space in memory.

If we were to use an assignment to increase the level variable, we would use:

    level += 1

The line basically means to take the value in the variable 'level' and increase it by one.

There are assignments for all operations:

    variable += 5 Add 5 to the value in variable
    variable -= 3 Subtract 3 from the value in variable
    variable *= 2 Multiply the value in variable by 5
    variable /= 4 Divide the value in variable by 4
    variable **= 2 Put the value in variable to the power of 2
    variable %= 5 Place the remainder of value in variable divided by 5

This can reduce the amount of typing for a line when performing such an operation.


#### 3.3. Comparison Operators

Sometimes we need to compare values or variables. These will be used more in 'if' statements, but we can show how this works now.

When we compare two values, we will get a result of 'True' or 'False'.

We have a few comparisons we can make:


- $==$ is equal to
- $!=$ is not equal to
- $>$ greater than
- $>=$ greater than or equal to
- $<$ less than
- $<=$ less than or equal to

So, I can test this with the command:

    print (10==20)

The answer would be 'False'. The statement is testing whether '10' is equal to '20', which it is not.
Now, I were to change it to:

    print (10 != 20)

The answer is True since '10' does not equal '20'.

The rest are simple comparative operations.

#### 3.4. Logical Operations

Sometimes we need to compare two or more conditions to determine if something must happen.

Let's assume two conditions. One condition for an example game is that the player must be level 10 or higher. The second condition is that the player must have over '100,000' points. If both conditions are met, then the player wins. The code may be similar to:

    ((level >=10) and (points >= 100000))

Notice that each condition is inside its own parenthesis. The whole statement, including the 'and', is enclosed in parenthesis.

If one of the conditions is not met, then the statement is 'False'. The only way for it to be 'True' is that both conditions are met.

We can also have two conditions that when either is met, just one or more, the statement is 'True'. Let's say that a player can win if they reach level 10 or get 100,000 points. The statement can also be 'True' if bot conditions are met. We should try an example:

    level=9
    points=100001
    print ((level >=10) or (points>=100000))

The result should be 'True'. Since the points are over '100,000', one condition is true so the whole statement is true.

Of course you can have more conditions than two to use the 'and' or the 'or' operator.

It is possible to combine 'and' with 'or' conditions.

We could assume that in a game, if a special award is granted to a player, they win. Our other stipulations still apply. The code would be:

    (((level>=10) and (points>=100000)) or (award==1))

If the following is the values of the variables:

    level=9
    points=100000
    award=0

Then the first condition, level>=10, is false. The second condition, points>=100000, is true. The last condition, award==1, is false.

The conditions are then:

    (((false) and (true)) or (false))

The 'and' portion is broken down as ((false) and (true)), which is then 'false'. To be 'true', both conditions must be true.

Now, we have the rest to handle, which is ((false) or (false)). For an 'or' operation, only one condition needs to be 'true' which they aren't. So, the whole statement in 'false'.

Let's try something a little different. What if we tried the following coding:

    level=9
    points=100000
    award=0
    print (level>=10 and points>=100000 or award==1)

What happens now?

The line will be processed the same as before. The reason is that 'and' conditions are tested before 'or' conditions. The way the parenthesis were used, made the 'and' condition tested first.

Be aware how you place the parenthesis.

The last logical operation is 'not'. Basically, if all of the '>' and '<' were backwards, then we would want the opposite to be found. So, what once was 'False' is now 'True' and what was 'True' is now 'False'. The statement would be:

    print (not(((level>=10) and (points>=100000)) or (award==1)))

What was 'False' is now reported as 'True'.


### 4. Flow Control

In this article, we will discuss the methods of managing the flow of statements in a program. These methods include:

- If
- For
- While

We will also cover two items that are used to exit these flow control items or to bypass an iteration of a loop.

- Continue
- Break

#### 4.1. If Statement

An 'if' statement is used to test information and determine what to do depending on the outcome of the test.

The standard syntax is: 'if (condition):'.

For instance, we can test if a value is within a certain range. Let's assume we want to test if a value is over 1000 and then increment another value. We will assume we have a variable named 'score' and if it is greater than 1000, we will increase the level and reduce the score value by 1000.

    if (score > 1000):
        level = level +1
        score = score - 1000

You can see that any lines to be included in the 'if' statement you indent. Once we do not indent any lines, we are out of the 'if' section.

We can also have an 'if-else' statement. We perform the 'if' check like before, but instead of performing code when the statement is true, we can also have a section to manage when the statement is false.

Let's assume we have a Number Guessing game. The program generates a random number into a variable named 'num'. We input a guess from the user that we compare to the random number. We place the guessed number in a variable named 'guess'.

    if (guess > num):
        print ("Your guess is too high, try lower.")
    else:
        print ("Your guess is too low, try higher.")

This gives you a basic idea, but we are missing the check to see if the guessed number is equal to the 'num'. The example is only to give you a taste of how flow control works. I'll include the code for a number guessing game towards the end of the article.

But what if we have multiple options to test? Let's look at the previous example and add in the option that the guess is correct.

    if (guess > num):
        print ("Your guess is too high, try lower.")
    elif (guess < num):
        print ("Your guess is too low, try higher.")
    else:
        print("You guessed the number!")

Here, you can initially test to see if our guess is greater than the random number. If the guess is greater, then we give a message that the guess was too great.

The second 'if' statement, an 'elif' statement, is testing if the guess is less than the random number. If this is true, we print a statement that the guess was too low.

The 'else' statement here will leave the only other option that the user guessed the number correctly.

#### 4.2. For Statement

A 'for-loop' is used to run through a loop of code a specific number of times.

Let's assume we have a game that has five levels. We can determine the level the user is on by testing the score. The values for the levels are 1000 increments. We will start at 5000 and go to 1000. Initially, we will set the value if the 'level' variable to '0'.

    level = 0
    a=[5000, 4000, 3000, 2000, 1000]
    for value in a:
        if (score > value):
            level = (value / 1000)

There are a few things going on here that we need to cover.

In the second line, we set the variable 'a' to the values for the level (5000, 4000, 3000, 2000, 1000). The term for this is a list. We assign a 'list' of numbers to the variable and we will access them one at a time.

The third line shows that we are using a 'for' loop and assigning an entry in the list of 'a' to the variable 'value'.

The fourth line is an 'if' statement to test if the 'score' is greater than the 'value' from the list. If the score is greater, then we set the 'level' to the value divided by 1000. The program changes the 'level' variable from '0' to '1', '2', '3', '4' or '5'. We assume that at level 5, we win the game.

After we set the value of 'level', we will have more code.

#### 4.3. While Loop

A 'while-loop' is used to perform a section of code an indeterminate amount of times.

Let's assume we have a game that we want to start out by playing a game and when done, ask the user if they want to play again. If the answer is yes, we will play again. We do not know how many games the user may want to play.

The code would be like:

    play = 0
    while (play == 0):
        # The game code goes here
        again = "a"
        while ((again != "y") and (again != "n")):
            again = input ("Do you want to play again? (y/n) ")
        if (again == "n"):
            play=1
    print ("Thanks for playing.")

We start out by setting the variable 'play' to '0'. We execute the game code while the variable 'play' is '0'. Once the user completes the game, we set a variable called 'again' to 'a'. While the variable is not 'y' and 'n', we ask the user to enter whether they want to play again. If the user does not enter 'y' or 'n', then a prompt appears for an answer. If the user enters a 'y', then the loop performed again, and the user plays again. Should the user enter 'n', then the variable 'play' has a value of '1' and the loop ends. The program prints a message thanking them for playing and the code ends.

The 'while' statement can also use an 'else' since we are testing for a condition. It is the same as an 'if-else' statement in function.

#### 4.4. Break

If we are inside one of the flow control methods, we can use 'break' to get out of the current method.

Just keep in mind the indenting for the methods. The 'break' command will exit the current indentation that contains the method that put the execution into that indent.

If we look at the number guessing game, we can use the 'if' statement to see if the number is too high, too low or correct. If the guess is correct, then we need to exit the 'if' statement:

        else:
            print ("You guessed the number!")
            win = 1
            break

The 'break' will exit the initial 'if' statement that the 'else' is connected to in the code.

#### 4.5. Continue

Instead of leaving a method, we can use 'continue' to skip the flow in the loop.

Let's say we have a 'for-loop' and we go through the code to increment a number when some condition is true.

If we hit the condition that is false, or it could be true depending on the code, we want to skip the loop and not perform the code. We test for the condition, and if needed, we issue the command 'continue' to go to the end of the loop and do the next iteration.

We can look back at a previous example and make a few changes:

level = 0
a=[5000, 4000, 3000, 2000, 1000]
for value in a:
     if (score <= value):
          continue:
     if (score > value):
          level = (value / 1000)

For entries that are less than or equal to the score, we can not even perform the remaining code.


#### 4.6. Number Guessing Game

Here is the Number Guessing game. The only lines that you may not know is the generation of the random number that is placed into 'num'.

The line 'from random import randrange' is used to set a random number and import into 'randrange'. We then use 'randrange' to generate a number from 0 to 99. We then add 1 to make the range 1 to 100. The program places the random number into the variable 'num'.

    play = 0
    while (play == 0):
        from random import randrange
        num = (randrange(99) + 1)
        win = 0
            while (win == 0):
            guess = input("Enter your guess (1 to 100): ") 
            guess = int(guess)
            if (guess > num):
                print ("Your guess is too high, try lower.")
            elif (guess < num):
                    print ("Your guess is too low, try higher.")
            else:
                    print ("You guessed the number!")
                    win = 1
                    break
        again = "a"
        while ((again != "y") and (again != "n")):
            again = input ("Do you want to play again? (y/n) ")
        if (again == "n"):
            play=1
    print ("Thanks for playing.")

Hopefully, this can help you use some of the flow control methods.


## More tools ...

- [Python tutorials](https://tarikgit.github.io/coding/index.html#_learning_to_code_in_python)
- [Learning python with OpenAI's ChatGPT](https://linux.org/threads/learning-python-with-openais-chatgpt.43802/)

## Sources

- [linux.org](https://linux.org/)
