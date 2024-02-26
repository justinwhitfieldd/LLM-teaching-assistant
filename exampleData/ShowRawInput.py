# ShowRawInput.py
""" Illustrates the raw_input function."""

x = raw_input('Enter any sequence of characters like abc: ')
y = x+x
print x,y

x = raw_input('Enter any sequence of characters that includes quotes like I\'m: ')
y = x+x
print x,y

x = raw_input('Enter a number like 5.1: ')
x = float(x)
y = x/3
print x,y

x = raw_input('Enter a number like 5.1: ')
y = x/3
print x,y

"""
Summary...

1. If you respond to a raw_input prompt then the
value returned is a string made up of exactly the
characters you entered in response to the prompt.

2. If you want to input a number, then you must convert
the imput sequence using int or float.
"""






