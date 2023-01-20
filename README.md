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

Task1 - Write a simple function which will transform a list of temperature values in Fahrenheit to a list of temperature values in Celsius. Use .map() function and lambda expression in this task.

Function signature: def to_celsius(temperature_list)

Your solution should contain Python code of the program.
You have to deliver Eclipse project contains your solution to Git repository for review.
Ask your tutor if you have any questions.

Task2 - Write a simple program to make a chain of function decorators for html text formatting (bold, italic, underline).

It should works like this:

@bold
@italic
@underline 
def get_text(): 
    return "hello world" 

print(get_text()) ## shows "<b><i><u>hello world</u></i></b>" 

Your solution should contain Python code of the program.
You have to deliver Eclipse project contains your solution to Git repository for review.
Ask your tutor if you have any questions.

Task3 - 1) For given function (with one parameter, parameter type and return value type are equal) generate another function that applies original fuction multiple times.

Example:

from math import sin
f1 = fn(lambda x: "sin(%s)" % x, 5)
f2 = fn(lambda x: sin(x), 5)
print("%s = %f" % (f1("1"), f2(1)))

>>sin(sin(sin(sin(sin(1))))) = 0.587181

print("%s = %f" % (f1("2"), f2(2)))

>>sin(sin(sin(sin(sin(2))))) = 0.606464

print(fn(lambda x: sin(x), 0)(1000))

>> 1000

Function signature: def fn(f, n)

2) Using 'fn' (see first part of the task) generate function that calculates golden ratio approximation.
Continued fraction theory (for curious):
https://ru.wikipedia.org/wiki/Непрерывная_дробь#.D0.A1.D0.B2.D0.BE.D0.B9.D1.81.D1.82.D0.B2.D0.B0_.D0.B8_.D0.BF.D1.80.D0.B8.D0.BC.D0.B5.D1.80.D1.8B
https://en.wikipedia.org/wiki/Continued_fraction
final formula:
1 + 1 / (1 + 1 / (1 + 1 / (...)))

some results:
golden_ratio(0) = 1
golden_ratio(1) = 2
golden_ratio(2) = 1.5
golden_ratio(100) = 1.6180...

Function signature: def golden_ratio(n), where 'n' is number of invocations (and number of terms in continued fraction)
Рабочая ссылка
https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%BF%D1%80%D0%B5%D1%80%D1%8B%D0%B2%D0%BD%D0%B0%D1%8F_%D0%B4%D1%80%D0%BE%D0%B1%D1%8C#.D0.A1.D0.B2.D0.BE.D0.B9.D1.81.D1.82.D0.B2.D0.B0_.D0.B8_.D0.BF.D1.80.D0.B8.D0.BC.D0.B5.D1.80.D1.8B


Task4 - Write a function that produces stream generator for given iterable object (list, generator, etc) whose elements contain position and value and sorted by order of apperance. Stream generator should be equal to initial stream (without position) but gaps filled with zeroes. For example:
>>> gen = gen_stream(9,[(4,111),(7,12)])
>>> list(gen) [0, 0, 0, 0, 111, 0, 0, 12, 0] # first element has zero index, so 111 located on fifth position, 12 located on 8th position
I.e. 2 significant elements has indexes 4 and 7, all other elements filled with zeroes.
To simplify things elements are sorted (i.e element with lower position should precede element with higher number) in initial stream.

First parameter can be None, in this case stream should be inifinite, e.g. infinite zeroes stream:
>>> gen_stream(None, [])
following stream starts with 0, 0, 0, 0, 111, 0, 0, 12, ... then infinitely generates zeroes:
>>> gen_stream(None, [(4,111),(7,12)])

Function should also support custom position-value extractor for more advanced cases, e.g.

def day_extractor(x):
  months = [31,28,31,30,31,31,30,31,30,31,30,31]
  acc = sum(months[:x[1]-1]) + x[0] - 1
  return (acc, x[2])

>>> precipitation_days = [(3,1,4),(5,2,6)]
>>> list(gen_stream(59,precipitation_days,day_extractor)) #59: January and February to limit output
[0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
precipitation_days format is following: (d,m,mm), where d - day in month, m - month, mm - precipitation in millimeters
So, in example:
(3,1,4) - January,3 precipitation: 4 mm
(5,2,6) - February,5 precipitation: 6 mm
Extractor passed as optional third parameter with default value - lambda function that handles (position, value) pairs like in first example.

Implementation hint:
you may need folowing built-in functions to iterate over input iterable object:
iter (https://docs.python.org/3/library/functions.html#iter), next (https://docs.python.org/3/library/functions.html#next)

Function signature: def gen_stream (total, sorted_iterable, extractor)

