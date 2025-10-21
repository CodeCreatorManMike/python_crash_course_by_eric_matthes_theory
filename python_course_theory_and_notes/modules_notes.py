# modules Notes

# NEW SECTION:
# os module - has functions to perform many tasks of operating systems
# NEW SECTION:

import os  # importing the os module

# mkdir() function:
# used to create a new directory (folder) in the given path
# The path should be given as a string and can be absolute or relative.
# Example below creates a folder named "tempdir" in D drive
# Uncomment the line below to actually create the folder.
# os.mkdir("d:\\tempdir")  # creates a new directory named tempdir inside D drive

# chdir() function:
# used to change the current working directory
# Example below changes the current working directory to D:\temp
# os.chdir("d:\\temp")

# getcwd() function:
# returns the name (path) of the current working directory
# print(os.getcwd())  # prints something like 'd:\\temp'

# Relative path example:
# if the current directory is D:\, we can just use folder name instead of full path
# os.chdir("temp")
# print(os.getcwd())  # prints 'd:\\temp'

# ".." means parent directory (one level up)
# os.chdir("..")
# print(os.getcwd())  # prints 'd:\\'

# rmdir() function:
# used to remove a specified directory
# NOTE: directory must be empty and not in use (not current directory)
# os.rmdir("d:\\tempdir")

# listdir() function:
# returns a list of all files and folders in the specified directory
# print(os.listdir("c:\\Users"))  # prints ['Public', 'Default', 'YourName', ...]


# NEW SECTION:
# random module - used to generate random numbers and selections


import random  # importing the random module

# random() function:
# returns a random float number between 0.0 and 1.0
# print(random.random())  # e.g. 0.755173688207591

# randint(a, b):
# returns a random integer between a and b (both inclusive)
# print(random.randint(1, 100))  # e.g. 58

# randrange(start, stop, step):
# returns a random element from the specified range (similar to range() function)
# print(random.randrange(1, 10))       # random number between 1–9
# print(random.randrange(1, 10, 2))    # random odd number between 1–9
# print(random.randrange(0, 101, 10))  # random multiple of 10 between 0–100

# choice(seq):
# returns a random element from a given sequence (string, list, or tuple)
# print(random.choice('computer'))           # e.g. 'o'
# print(random.choice([12, 23, 45, 67]))     # e.g. 67
# print(random.choice((12, 23, 45, 67)))     # e.g. 23

# shuffle(list):
# randomly reorders elements in a list (in-place)
numbers = [12, 23, 45, 67, 65, 43]
# random.shuffle(numbers)
# print(numbers)  # list is now randomly shuffled


# NEW SECTION:
# math module - provides mathematical functions and constants


import math  # importing the math module

# Constants:
# math.pi -> value of π (pi) = 3.141592653589793
# math.e  -> Euler’s number = 2.718281828459045
# print(math.pi)
# print(math.e)

# radians() function:
# converts angle in degrees to radians (used by trigonometric functions)
# print(math.radians(30))  # 0.5235987755982988

# degrees() function:
# converts angle in radians to degrees
# print(math.degrees(math.pi/6))  # 29.999999999999996 ≈ 30°

# Trigonometric functions:
# need angle in radians
# print(math.sin(math.radians(30)))  # 0.5
# print(math.cos(math.radians(30)))  # 0.8660
# print(math.tan(math.radians(30)))  # 0.5773

# log() function:
# returns natural logarithm (base e)
# print(math.log(10))

# log10() function:
# returns base-10 logarithm
# print(math.log10(10))  # 1.0

# exp() function:
# returns e raised to given number (e**x)
# print(math.exp(2))  # 7.389...

# pow() function:
# raises first number to the power of the second
# print(math.pow(4, 4))  # 256.0

# sqrt() function:
# returns the square root of the given number
# print(math.sqrt(100))  # 10.0

# ceil() and floor():
# ceil() rounds up to nearest integer
# floor() rounds down to nearest integer
# print(math.ceil(4.568))  # 5
# print(math.floor(4.568))  # 4


# NEW SECTION:
# sys module - interacts with the Python runtime environment


import sys  # importing sys module

# sys.argv:
# returns list of command line arguments passed to the script
# Example:
#   python test.py Anil 23
# sys.argv[0] = script name, sys.argv[1] = 'Anil', sys.argv[2] = '23'
# print("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))

# sys.exit():
# safely exits the program
# sys.exit()

# sys.maxsize:
# returns the largest integer value a variable can take
# print(sys.maxsize)  # e.g. 9223372036854775807

# sys.path:
# returns list of directories Python searches for modules
# print(sys.path)

# sys.stdin, sys.stdout, sys.stderr:
# file objects for input, output, and error messages

# sys.version:
# returns the version of Python interpreter being used
# print(sys.version)


# NEW SECTION:
# collections module - provides alternatives to built-in container types


import collections  # importing collections module

# namedtuple() function:
# creates tuple subclass with named fields
# Syntax: collections.namedtuple(typename, field_list)
# Example:
# employee = collections.namedtuple('employee', ['name', 'age', 'salary'])
# e1 = employee("Ravi", 25, 20000)
# print(e1.name)  # access by name
# print(e1[0])    # access by index

# OrderedDict() function:
# remembers the insertion order of keys
# d2 = collections.OrderedDict()
# d2['A'] = 20
# d2['B'] = 30
# d2['C'] = 40
# for k, v in d2.items():
#     print(k, v)

# deque() function:
# double-ended queue, allows fast append/pop from both ends
# q = collections.deque([10, 20, 30, 40])
# q.appendleft(110)  # adds to left
# q.append(41)       # adds to right
# print(q)
# q.pop()            # removes from right
# q.popleft()        # removes from left
# print(q)


# NEW SECTION:
# statistics module - provides basic statistical functions


import statistics  # importing statistics module

# mean():
# calculates arithmetic mean (average)
# print(statistics.mean([2, 5, 6, 9]))  # 5.5

# median():
# returns middle value (if even number of elements, returns average of middle two)
# print(statistics.median([1, 2, 3, 8, 9]))  # 3
# print(statistics.median([1, 2, 3, 7, 8, 9]))  # 5.0

# mode():
# returns most frequent value
# print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2]))  # 2

# stdev():
# returns standard deviation of a sample
# print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]))


# NEW SECTION:
# time module - handles time and date operations


import time  # importing time module

# time():
# returns current time in seconds since epoch (Jan 1, 1970)
# print(time.time())

# localtime():
# converts seconds since epoch to a struct_time object (readable format)
# tk = time.time()
# print(time.localtime(tk))

# asctime():
# converts struct_time into a readable string format
# tp = time.localtime(time.time())
# print(time.asctime(tp))

# ctime():
# returns current time as a readable string directly
# print(time.ctime())

# sleep():
# pauses program execution for given seconds
# print("Program paused for 5 seconds...")
# time.sleep(5)
# print("Program resumed!")
