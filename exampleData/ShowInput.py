# ShowInput.py
""" Illustrates the input function."""

x = input('Enter a float like 5.1: ')
y = x/3
print x,y

x = input('Enter an int like 8: ')
y = x/3
print x,y

x = input('Enter a number in quotes like \'-5.2\': ')
y = x+x
print x,y

x = input('Enter a general string like \'abc\': ')
y = x+x
print x,y

x = input('Enter a string without quotes like abc: ')
y = x+x
print x,y

"""
Summary...

1. If you respond to an input prompt with a decimal
number, it will return a float.

2. If you respond to an input prompt with an integer
number, it will return an int.

3. If you respond to an input prompt with a single-quoted string,
it will return a string.

4. If you respond to an input prompt with an unquoted sequence
of characters that is not a number, then (usually) an error results.
"""











