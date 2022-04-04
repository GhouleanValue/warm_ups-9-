# Introduction to def key word.

# This is where I have ran in to the most problems learning to code. The options available for us to do what we want, rapidly expands with the def keyword/user defined function.

# Be patient and persistent in using def keywords and you will get past this learning curve.

# For this reason, the next 4 or so entries in the beginner warmups will probably be associated with user defined functions.

# The last thing ill say before we get started is a lot of what I have learned regarding Python is from the zero to hero bootcamp by perian data  on Udemy.

# The rest of what I have learned, is either by myself or from Youtube. So if you feel lost with this section of python use these resources!


#1 | Functions

def say_hello(name='Default'):
    print(f'hello {name}')

print(say_hello('Jim'))

#return allows you to save as a variable vs the print function reprinting what ever is in the ().


#2 | Functions

def even_check(number):
    result = number % 2 == 0
    return result

    even_check(20)

print(even_check(20))

# then try an odd number

even_check(21)

#3 | Functions

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
    else:
        pass

    return False

print(check_even_list([1, 3, 5]))

# Try another list

print(check_even_list([1, 1, 2]))

# If you are using Jupiter notebook, you do not need to use the print function to see your output in the output window.
