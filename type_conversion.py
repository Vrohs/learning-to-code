# we can use int() function to convert a string into int data type.
# similarly, float() converts into floating point value.
# and bool() converts it into boolean value.
# type() function will tell you the data type of a particular variable.

year_born = input('enter your YOB\n')
current_age = 2023 - int(year_born)    #using the int function
print("you're",current_age, "years old")
print(type(year_born))
print(type(current_age))
