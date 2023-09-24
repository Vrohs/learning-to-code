# exploring *args and **kwargs in python

def myfunc(a, b):
    return sum((a, b)) * 0.05

print(myfunc(40, 60))

# *args allows you to pass in an arbitrary number of arguments to a function
# the *args parameter is a tuple of the arguments passed in
# you can name the parameter anything you want, but *args is the convention
# you can also pass in a list of numbers to the function
# the * operator unpacks the list into individual arguments

def myfunc(*args):
    return sum(args) * 0.05 # sum is a built-in function in python

print(myfunc(40, 60, 100, 1, 34))

# **kwargs allows you to pass in an arbitrary number of keyword arguments to a function
# the **kwargs parameter is a dictionary of the keyword arguments passed in
# you can name the parameter anything you want, but **kwargs is the convention
# you can also pass in a dictionary of numbers to the function
# the ** operator unpacks the dictionary into individual arguments

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit'])) 
    else:
        print('I did not find any fruit here')

myfunc(fruit = 'apple', veggie = 'lettuce')
