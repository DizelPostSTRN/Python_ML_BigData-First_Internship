This is a copy of my repository from an internship at the company '......'

Some assignments have been lost.

The internship process was based on the book "The Quick Python Book - 3 edition". Below are links to the book and other sources.


====== ch04_basics =====

The mission itself is lost.


=====ch05_collections =====

Read chapter 5 of the "The Quick Python Book - 3 edition".

Task1 - Write a function that removes the three largest elements from an integer list (list size >= 3) and returns a list of the results. If the largest element is not unique at some step, remove the one closest to the end of the list. The original list should not change.

Task2 - Write a function that takes 4 lists of numbers and outputs the number of unique ones.

Task3 - Write a function that takes two lists of positive numbers and outputs the largest ordinary number, or zero if the total number is not found.


===== ch06_strings =====

Read chapter 6 - Strings of The Quick Python Book
Covered topics:
■ Understanding strings as sequences of characters
■ Using basic string operations
■ Inserting special characters and escape sequences
■ Converting from objects to strings
■ Formatting strings
■ Using the byte type
note: reading formatting sections is optional

The mission itself is lost.


===== ch07_dictionaries =====

Read chapter 7 - Dictionaries of The Quick Python Book
Covered topics:
■ Defining a dictionary
■ Using dictionary operations
■ Determining what can be used as a key
■ Using dictionaries as caches
note: reading 7.5 Sparse matrices and further sections is optional

Task1 - Write a function that creates swapped dictionary (keys and values interchanged) for given dictionary.
In original dictionary multiple keys may refer to the same value, so, new value should be tuple with all corresponding keys.
Example: dictionary {1:2, 3:4, 5:4, 7:2, 9:4} swapped to {2: (1, 7), 4: (3, 9, 5)}
Hint: use 'for' loop like in book's section 7.3
Function signature: def swap_dict(d)
Your solution should contain Python code of the program.
You have to deliver Eclipse project contains your solution to Git repository for review.
Ask your tutor if you have any questions.

Task2 - Write a function that creates compact version of dictionary.
In compact dictionary keys are grouped by original dict's values into tuples.
Example: dictionary {1:2, 3:4, 5:4, 7:2, 9:4} compacted to {(3, 9, 5): 4, (1, 7): 2}
Hint: use 'for' loop like in book's section 7.3
Function signature: def compact_dict(d)
Your solution should contain Python code of the program.
You have to deliver Eclipse project contains your solution to Git repository for review.
Ask your tutor if you have any questions.


===== ch08_control_flow =====

Read chapter 8 - Control flow of The Quick Python Book
Covered topics:
■ Repeating code with a while loop
■ Making decisions: the if-elif-else statement
■ Iterating over a list with a for loop
■ Using list and dictionary comprehensions
■ Delimiting statements and blocks with
indentation
■ Evaluating Boolean values and expressions

Task1 - Write a function to calculate required capacity of transport hub by provided schedule and observation period.

Each transport vehicle that visits the hub described by two parameters: 1) period (n means that transport visits hub every n days), 2) amount of goods transport can take. Each vehicle belongs to one of following types: if 2) is positive vehicle is producer
(delivers goods to hub), otherwise - consumer (takes goods from hub).

Delivery model:
a) each day number (zero or more) of producers and number (zero or more) of consumers
visit the hub
b) producers always deliver amount of goods equal to its capacity
c) consumers always take all available goods up to its capacity (e.g. if vehicle capacity=3 and available on hub=7 vehicle will take 3; if capacity=3, on hub=2 , vehicle will take 2), if required consumers wait producers till the end of the day to take as much goods as possible
d) each day vehicles can visit hub in any order (not dependent on vehicle order in schedule), so more goods can be observed on hub during the day than at the end of day

The task is to find minimum hub capacity such that producers always will have place to ship off their cargo during observation period.

Schedule format: list of strings, each string is period and capacity (negative for consumers) separated by space.

Example: schedule ["2 -2", "3 3"], number of observed days 7
transport hub capacity: 4
calculated in following way: (day: 1, goods on hub at the end of day: 0), (2, 0), (3, 3), (4, 1), (5, 1), (6, 2), (7, 2) -- max amount on day 6, because producer can arrive earlier


Function signature: def transport_hub (schedule, days)
Function result: integer number (transport hub capacity)

Your solution should contain Python code of the program.
You have to deliver Eclipse project contains your solution to Git repository for review.
Ask your tutor if you have any questions.


===== ch09_functions =====

Read chapter 9 - Functions of The Quick Python Book
Covered topics:
■ Defining functions
■ Using function parameters
■ Passing mutable objects as parameters
■ Understanding local and global variables
■ Creating and using lambda expressions
■ Using decorators



