# String Formatting
user_name = "sarah_1987"
age = 23
output = '{} is {} years old'.format(user_name, age)
print(output)

# input
friends = int(input("How many friends are at your house?"))
piazzas = friends * 0.5
print("You need {} pizzas for {} friends".format(piazzas, friends))

"""
Python Modules
Modules: Code that someone else has written that you can reuse in your programs
        - user-defined or built-in
        - Modules are imported into your Python programs
        - e.g. math -> mathematical functions
               datetime -> date and time value manipulation
               timeit -> time the execution of small blocks of Python code
               re -> regular expressions (pattern search)
               copy -> duplicating objects
                
"""
import datetime
x = datetime.datetime.now()
print(x)

# Formatting Date objects
my_date = datetime.date(2020, 1, 31)
print(my_date.strftime("%d-%b-%Y"))

"""
Character codes
%a: Returns the first three characters of the weekday. [Wed]
%A: Returns the full name of the weekday. [Wednesday]
%B: Returns the full name of the month. [September]
%w: Returns the weekday as a number, from 0-6, with Sunday being 0
%m: Returns the month as a number, from 01 to 12
%p: Returns AM/PM for time
%f: Returns microsecond from 000000 to 999999
%Z: Returns the timezone
%Y: Returns the year in four digit format. [2022]
%b: Returns the first three characters of the month name. [Dec]
%d: Returns day of the month, from 1 to 31.
%H: Returns the hour.
%M: Returns the minute, from 00-59.
%S: Returns the second, from 00-59.
"""

"""
For loops
- used to iterate over sequences (a collection of items)
- any iterable objects can also be traversed
"""
for number in range(5):
    print(number)

for character in "Banana":
    print(character)

for name in ["Mary", "Ranjit", "Fatima"]:
    print(name)

"""
While loop
- used to iterate over a block of code or statements as long as the test expression is true
- user does not know beforehand how many iterations are going to take place
- if infinitely loop -> run out of memory usage
"""

# Example 1: due to social distancing, only 10 people are allowed to be inside a shot at the same time.
store_capacity = 10
while store_capacity > 0:
    print("Please come in. Spaces available: " + str(store_capacity))
    store_capacity -= 1      # infinite loop without this
print("Please wait for someone to exit the store.")


"""
Functions: reusable block of code that contains one or more Python statements and used for performing a specific task

1. Code re-usability
2. Improves readability
3. avoid redundancy

Types of Arguments
- Default arguments
- Variable Length Positional arguments (*args)
- Variable Length Keyword Arguments (**kwargs)
"""
# 1. Positional arguments - pass arguments in the order in which they are defined
def some_function(job, name):
    print(name, "is a ", job)
some_function('developer', "Fiona")

"""
2. Keyword arguments
- pass arguments using the names of their corresponding parameters
- order of arguments doesn't matters
- can combine positional and keyword arguments in a single call (specific the positional arguments before keyword arguments)
"""
def some_function(name, job):
    print(name, "is a ", job)
some_function(job="developer", name="Fiona")
some_function(name="Fiona", job="developer")

"""
Default Arguments
- You can specific default values for arguments when defining a function
- default value is used IF the function is called without a corresponding argument
"""
def some_function(name, job="developer"):
    print(name, "is a ", job)
some_function("Fiona")
some_function("Fiona", "manager")

# random: built-in library for random data
import random
random_integer = random.randint(1, 100)
print(random_integer)

# randint(): generates a random number between two values
sides = int(input("How many sides does the die have?"))
random_integer = random.randint(1, sides)
print("You rolled a {}".format(random_integer))


"""
List: an ordered collection of values
Diectionary: Stores a collection of labelled items. Each item has a key and value
"""
place = {
    "name": "The Anchor",
    "post_code": "E14 6HY",
    "street_number": "54",
    "Location": {
        "longitude": 127,
        "latitude": 63,
    }
}
print("longtitude, latitude: {}, {}".format(place["Location"]["longitude"], place["Location"]["latitude"]))

# choice(): returns a random item from a list
colours = ['red','green', 'blue']
chosen_color = random.choice(colours)
print(chosen_color)

# Writing to a txt file
with open("people.txt", "w+") as text_file:
    people = "Joanne \nSusan \nAmina"
    text_file.write(people)

# Reading from a txt file
with open("people.txt", 'r') as text_file:
    contents = text_file.read()
print(contents)

# Writing a CSV file
import csv
field_names = ["name", "age"]
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28}
]
with open('team.csv', "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# Reading a CSV
with open("team.csv", "r") as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    print("Print from team.csv: ")
    for row in spreadsheet:
        print(dict(row))

"""
pip: a package manager used to install libraries that other people have written (use in terminal)

Application Programming Interface (API): 
- a way for different programs to interact. For example they can send data to one another
- Web APIs allows you to interact with other programs over the internet.

                request
Your computer -----------> The Internet -----------> API
              <-----------              <-----------
                                            Response
                                            
API request: when your program asks an API for some or to complete a specific action
API Response: The result of your request from the API


Response status code:

"""
import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID?")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon)