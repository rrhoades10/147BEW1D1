print("Hello, world!")

# Creating a variable in python
# Variable is a name that we make up that is going to store some kind of data
# It should be relevant to whatever the data is
name = "Ryan" # name is our variable because Ryan is a name

greeting = "Hello, there!"

response = "General Kenobi"

print(name)
print(greeting)
print(response)

# all caps tells us this is a constant variable - which should not change
CLASS_WEEKS = 4
print(CLASS_WEEKS)
# CLASS_WEEKS = 5 #we can reassign but we shouldn't
# print(CLASS_WEEKS)

#snake case, an underscore for each space
cool_game = "Baldurs Gate 3" 
# print(cool_game)
# control (or command) slash to comment out a single line or multiple lines of code

# Some number and math stuff!
# Floats and Integers
# Integer is a whole number in python, 3, 4, 102
# Float is a decimal number 3.14, 6.5

# Integer
number = 5 # declaring an integer 
print(number)

# Float
decimal = 3.14
print(decimal)

# the variable names do not matter BUT MAKE THEM RELEVANT
# number is not what is making 5 a number, the fact that its a 5 is doing that
lemur = 5 # still a 5
duck = 3.14 # still 3.14

# DOING SOME MATH \(￣︶￣*\))
# addition
strawberries = 10
blueberries = 5
mixed_fruits = strawberries + blueberries
print(mixed_fruits)
# 15 = 10 + 5 setting this sum of two numbers to a variable name
# subtraction
slices_of_pizza = 8
slice_taken = 4
pizza_left = slices_of_pizza - slice_taken
# 4 = 8 - 4
print(pizza_left)
# multiplication
party_guests = 25
slices_per_guest = .5 
total_slices = party_guests * slices_per_guest
print(total_slices)
# division
pie_slices = 8
people_at_table = 4
slices_per_person = pie_slices/people_at_table
print(slices_per_person)

# using round()
print(round(7/3))
# floor division - round down to the nearest whole number // -- double slashes
# always rounds down to the nearest whole number
total_sandwiches = 7
people = 3
sammies_per_person = round(total_sandwiches//people)
print(sammies_per_person)
# modulo
# exponetiation 

from math import ceil
print(ceil(5.1))

# Modulo % --> returns the remainder of a division problem
cookies = 14 #chocolate chip cookies
cookies_per_person = 5
cookies_left = cookies % cookies_per_person
print(cookies_left)

# checking if a number is even (or if a number is divisible by another number)
number = 12
# extra conditional sauce
if number % 2 == 0:
    print("Thats an even number")
else:
    print("Thats an odd number")

if number % 3 == 0:
    print("Fizz")

# Exponents -> **
tea_strength = 2
#              original num - to the - somethign power 
cups_of_tea = tea_strength ** 4
print(cups_of_tea)

# ==================== BOOLEAN OPERATORS ==========================
# == -> Equal to
# < -> less than
# > -> greater than
# != -> not equal
# <= -> less than or equal to
# >= -> greater than or equal to

# Boolean is True or False
num1 = 5
num2 = 7
num3 = 12
num4 = 5
print(num1 == num4) # True num1 is equal to num4
print(num2 < num1) # False num2 is not less than num1
print(num3 > num2) # True num3 is greater than num2
print(num1 != num3) # True num1 is not equal to num3
print(num3 <= num4) # False num3 is not less than or equal to num4
print(num1 >= num4) # True num1 is greater than or EQUAL TO num4

if num3 > num1: #is this a True statement
    print("Num3 is greater!") # if so do this
    print("Num3 is greater!")
    print("Num3 is greater!")
    print("Num3 is greater!")
    print("Num3 is greater!")
    print("Num3 is greater!")
    print("Num3 is greater!")
    print("Num3 is greater!")

else: #otherwise
    print("Num3 is not greater!") #do this

# ==================== INDENTATION ========================
# Indentation in python defines blocks of code
# 4 spaces or tab
name = "Lando"
if name == "Lando":
    print("How could you have betrayed Han!?!?!!")
if name != "Ryan": #iterpretter sees colon and expects an indented block beneath it
    print("blah blah")
    print("more stuff")
    print("other things")
    print("hello")

# Some examples of bad indentation
if True:
    print("This is great!")
#   print("Oh no a sneaky tab")

# Unexpected Indent
print("They're taking the hobbits to Isengard")
    # print("What about second breakfast")

# Expecting an ident
# if True:
# print("I should be indented")

# weather = "sunny"
# if weather == "sunny":
#     print("wear sunglasses")
#     if clouds == True:
#         print("wear extra sunscreen cause thats where the harmful rays cvome from or something")
#         if temperature == "hot":
#             print("drink lots of water")
#             if pavement == "blacktop":
#                 print("make sure your dog has booties on")
# else:
#     print("Take an umbrella")

# creating a code comment
# prevents the interpretter from reading that code 

# Mult-line statemetn - Docstring
# """This is great for writing comments or strings that take up several lines"""
my_string = """I can write in here
and take up as many
lines as i would like """
print(my_string)
# also use them to write haikus in python

# using blackslashes for line continuation
# for strings that may take up more than one line
backslash_string = "Hello there! I hope \
you're having a nice time learnign python! \
and if youre not, well thats too damn bad!"
print(backslash_string)

# you can use double quotes and single quotes interchangeably 
name = "Ryan"
name = 'Ryan'
sentence = "My dog's name is Eyo"

# ================= Python Casing =====================
# casing matters whether its for variable names or strings
name = "Ryan"
Name = "Victor"
print(name)
print(Name)
# name and Name are not the same variable
# case sensitivty in strings
print("Hello" == "hello")
print("hello" == "hello")
print("Hello" == "Hello")

# ================= using the python input() function ===============================
# input("to be displayed in your terminal or command line")
# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# quest = input("What is your quest? ")

# formatted string
# print(f"My name is {name}, my favorite color is {color} and my quest is {quest}")


# input in terms of collecting a user input
# input - a function takes something as an input
#                     parameter
# def do_something(input goes here):
    # do somethign else

#==================== TYPE CASTING ========================
# number = input("Give me a number! ")
# print(5 + number)

my_string = "Hello " + "There"
print(my_string)
# using type()
# print(type(number))

name = "Ryan"
print(type(name))

integer = 6
print(type(integer))

decimal = 3.14
print(type(decimal))

# adding integer and decimal
print(integer + decimal)
# adding an integer or decimal to a string
# print(name + integer)

# changing types
# int() turn valid types into integers
# float() turn valid types into floats
# str() turn valid types into strings
# number = input("Give me a number! ") # assings number variable to whatever is entered by the user
number = "5"
print(type(number))
# since the input defaults to returning a string
# we change the type from a string to an integer
# and reassign the number variable
number = int(number)
print(type(number))
print(number + 16)

# number = int(input("Give me a number! ")) #collects user input and casts to an integer

# changing floats to integers and integers to floats
decimal =  54.67
print(type(decimal))
# converting a decimal to an integer
whole_number = int(decimal)
print(whole_number)
print(type(whole_number))

# changing an integer to a float
integer = 67
print(type(integer))
new_float = float(integer)
print(new_float)
print(type(new_float))

print(round(decimal, 0))

# Python is Dynamically Typed
# i can set a variable to any type and i can reassign that variable to any other type
my_variable = "Top of the mornign to ya"
print(type(my_variable))

my_variable = 14
print(type(my_variable))

# ============= single line variable assignment ====================
# name = "Sebulba"
# animal = "duck"
# robot = "Mega Man"

name, animal, robot = "Duck", "Duck", "Duck"
print(name)
print(animal)
print(robot)
name = "Duck"
animal = "Duck"
robot = "Duck"
if name == animal:
    print("Theyre equal")

a, b, c = ["duck", "duck", "duck"]
print(a)
print(b)
print(c)

# name = animal = robot = "Duck"
name = "Duck"
animal = name
robot = animal
# is checks if two things are pointing to the same location in memory
if animal == name:
    print("yeah thats a duck")

print(animal==name)

if animal is name:
    print("They point to the same spot")

if robot is animal:
    print("Robot is animal")

if robot is name:
    print("Robot is name")

animal = "Duck"
bird = "Duck"
if bird is animal:
    print("Animal is bird")
else:
    print("They are not at the same location")
# == != is
# == is for equality
# is -> for location, a variable pointing to another variable
print(animal==bird)

# id -> we can use to see the location of a variable
vegetable = "Tomato"
print(id(vegetable))

def say_hello():
    return "hello"

print(say_hello)

num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 4, 5]

num3 = num2

if num3 is num2:
    print("Is is not working")
else:
    print("Yay it worked")

name = "Ryan"
number = 16
# TypeError
# print(number + name)

# ZeroDivisionError
# zero_error = 10 / 0

# AttributeError
# error that occures when we try to access an objects attribute or method that doesnt exist
print(type(number))
print(type(name))
# new_number = number.split()

# Logic Errors
# situations where our code doesnt quite add up
# check for an even number
number = 6
if number % 2 == 0:
    print(True)
else:
    print(False)

# return a list of only even numbers
input_list = [1,2,3,4,5,6,7,8,9,10]
cool_list = [11, 12, 13, 14, 15, 16 ,17 ,18 ,19, 20]
neat_list = [21,22,23,24,25,26,27,28,29,30]
#             parameter - a placeholder variable for an argument
def even_nums(alist):
    even_list = []
    for num in alist:
        if num % 2 == 0:
            # return num
            even_list.append(num)
    return even_list

print(even_nums(input_list))
print(even_nums(cool_list))
print(even_nums(neat_list))

# in keyword
# use this to check for memebership inside of iterables
# strings, dictionarys, lists, tuples, you name we're in it
name = "Obi Wan"
if "b" in name:
    print("Theres a b here")

name_list = ["Chris", "Farzin", "Winter", "Victor", "Kayla"]

if "Lando" in name_list:
    print("Hes here")
else:
    print("NOPE")

if "Victor" in name_list:
    print("Yay Victor's here! Thanks Victor!")

sentence = "big b little b what begins with b barber baby bubble and a bumble bee"
b_count = 0
for letter in sentence:
    if letter == "b":
        b_count += 1 # increments the b_count
        # b_count = b_count + 1
print(b_count)

print(len(sentence.split("b"))- 1)

b_list = sentence.split("b")
print(b_list)
print(len(b_list))
 #    0    1         2         3          4            6    6     7     8    9     10   11    12          13    14    15       
b = ['', 'ig ', ' little ', ' what ', 'egins with ', ' ', 'ar', 'er ', 'a', 'y ', 'u', '', 'le and a ', 'um', 'le ', 'ee']

