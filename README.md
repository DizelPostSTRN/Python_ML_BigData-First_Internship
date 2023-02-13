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


===== ch14_exceptions =====

You have the following function:
def retrieve_age(person):
  return int(person["age"])


Modify this function to handle possible exceptions.

===== Parser MP3 ======

Function signature: def parse_id3v2(file_path)
Format description:
•	ID3v2 tag contains metadata(artist, album name, song name, etc) of MP3 file.
•	usually (otherwise, don't parse) MP3 files start with ID3v2 tag, then audio data follows
ID3v2 tag consists of header and body, header (10 bytes in total):
ID3v2/file identifier "ID3" 
ID3v2 version $04 00 (ID3v2 version 4), $03 00 (ID3v2 version 3)
ID3v2 flags %abcd0000 (1 byte, if `b` is set - extended header present)
ID3v2 size 4 * %0xxxxxxx (4 bytes, first bit of each byte always 0, 28 effective bits in total)
example:
b'ID3\x03\x00\x00\x00\x00\x03\x19'
     ID3v2/file identifier      b'ID3' (b'ID3' - the way Python handle binary data in ASCII range, equal to b'x49x44x33')
     ID3v2 version              $03
     ID3v2 flags                $00
     ID3v2 size                 $00 00 03 19 = 409 bytes
•	tag body consists of one or more frames, followed one after another
•	tag frame consists of header and body (with actual data)
header (10 bytes in total), size format differs for ID3v2 version 3 and version 4:
Frame ID $xx xx xx xx (four ASCII characters)
Size (v4) 4 * %0xxxxxxx
size (v3) $xx xx xx xx (32 effective bits in total)
Flags $xx xx
example:
b'TYER\x00\x00\x00\x05\x00\x00\x002004'
Frame ID       b'TYER'
Size           $00 00 00 05 = 5 bytes
Flags          $00 00
Data           $00 b'2004' -- first byte - encoding (see below), followed by data (year of release)
There are several frame types. One of them, text information frames (identified by Frame ID starting with 'T' as in example above) should be parsed and binary data converted to string.
Text frame body format:
•	first byte is encoding, values:
$00 – ISO-8859-1 (LATIN-1, Identical to ASCII for values smaller than 0x80).
$01 – UTF-16 (UCS-2) encoded Unicode with BOM, in ID3v2.2 and ID3v2.3.
$02 – UTF-16BE encoded Unicode without BOM, in ID3v2.4.
$03 – UTF-8 encoded Unicode, in ID3v2.4.
•	then actual data follows
To convert to string use `decode` function, e.g. in REPL:
>>> b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, Python 3!'.decode('UTF-8')
'Привет, Python 3!'
Implementaion notes:
•	this is educational task, don't implement all features described in specification, just what required in task
•	ensure your file starts with ID3 tag
•	ensure ID3v2's version is 3 or 4
•	don't parse files with extended header
•	realworld ID3 tags can be incorrectly constructed, be careful (use Python 'with' construct to open file, exceptions should be handled)
•	if it's not possible to parse file (for any reason: file not exists, no file read access, bad format, etc) return empty list
•	read only tag data from file, don't read it all, this decreases IO dramatically (2.5 VS 27 seconds on my 1.6 GB directory with MP3s)
•	it's ok to use "magic numbers" while parsing structures, e.g. version (major) occupies byte 4 in ID3 header, so can be accessed in following way: tag_header3 (compare with tag_header_offset = 3; tag_header[tag_header_offset])
•	you may use hex editor to investigate file content
•	see attached doc for more details
Your function should return list of tuples (in order of appearance) with tag data, tuple format:
•	Frame ID
•	size
•	binary data
•	for text fields data converted to string, otherwise None
Examples:
 >>> parse_id3v2('ariya_ulitsa_roz.mp3')
[(b'TIT2', 19, b'\x03\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb7\x00', 'Улица роз\x00'), (b'TALB', 29, b'\x03\xd0\x93\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb9 \xd0\xb0\xd1\x81\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\x00', 'Герой асфальта\x00'), (b'TCON', 13, b'\x03Heavy Metal\x00', 'Heavy Metal\x00'), (b'TDRC', 6, b'\x001987\x00', '1987\x00'), (b'TRCK', 5, b'\x005/6\x00', '5/6\x00'), (b'TPE1', 10, b'\x03\xd0\x90\xd1\x80\xd0\xb8\xd1\x8f\x00', 'Ария\x00')]

>>> parse_id3v2('01_epidemiya_pridumai_svetlii_mir_myzuka.me.mp3')
[(b'TALB', 61, b'\x01\xff\xfe\x1f\x04@\x048\x044\x04C\x04<\x040\x049\x04 \x00A\x042\x045\x04B\x04;\x04K\x049\x04 \x00<\x048\x04@\x04 \x00(\x00S\x00i\x00n\x00g\x00l\x00e\x00)\x00', 'Придумай светлый мир (Single)'), (b'TCON', 25, b'\x01\xff\xfeP\x00o\x00w\x00e\x00r\x00 \x00M\x00e\x00t\x00a\x00l\x00', 'Power Metal'), (b'TIT2', 43, b'\x01\xff\xfe\x1f\x04@\x048\x044\x04C\x04<\x040\x049\x04 \x00A\x042\x045\x04B\x04;\x04K\x049\x04 \x00<\x048\x04@\x04', 'Придумай светлый мир'), (b'TPE1', 19, b'\x01\xff\xfe-\x04?\x048\x044\x045\x04<\x048\x04O\x04', 'Эпидемия'), (b'TRCK', 13, b'\x01\xff\xfe0\x001\x00/\x000\x004\x00', '01/04'), (b'TYER', 11, b'\x01\xff\xfe2\x000\x001\x006\x00', '2016'), (b'TSSE', 13, b'\x03Lavf51.12.1\x00', 'Lavf51.12.1\x00'), (b'APIC', 58516, b'\x00image/jpg\x00\x03\x00\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xfe\x00?CREATOR: gd-jpeg v1.0 (using IJG JPEG v80), default quality\n\x00\xff\xdb  ... #50kilobytes of hex data removed from example# ', None), (b'COMM', 34, b'\x01eng\xff\xfe\x00\x00\xff\xfe(\x00m\x00y\x00z\x00u\x00k\x00a\x00.\x00o\x00r\x00g\x00)\x00', None)]

