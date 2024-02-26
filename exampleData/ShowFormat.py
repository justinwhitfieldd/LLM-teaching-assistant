# ShowFormat.py
""" Illustrates formatted print. You are
never tested on this stuff. It is just handy in
assignments when you to display floats, ints,
and strings and want things to look nice.
"""

# The f-format

x = 1234.123456789
print '\nThe f-format (decimal notation)'
print '\n%m.nf means allocate m spaces overall with n to the right of the decimal.'
print 'The number is right-justified within the space allocated.\n\n'
print 'x = %16.3f' %x
print 'x = %16.6f' %x
print 'x = %16.9f' %x

print '\n%-m.nf means allocate m spaces overall with n to the right of the decimal.'
print 'The number is left-justified within the space allocated.\n\n'
print 'x = %-16.3f' %x
print 'x = %-16.6f' %x
print 'x = %-16.9f' %x

# The e-format

x = 1234.123456789
print '\nThe e-format (scientific notation)'
print '\n%m.ne means allocate m spaces overall with n to the right of the decimal.'
print 'The number is right-justified within the space allocated.\n\n'
print 'x = %16.3e' %x
print 'x = %16.6e' %x
print 'x = %16.9e' %x

print '\n%-m.ne means allocate m spaces overall with n to the right of the decimal.'
print 'The number is left-justified within the space allocated.\n\n'
print 'x = %-16.3e' %x
print 'x = %-16.6e' %x
print 'x = %-16.9e' %x

# The d-format
x = 123456789
print '\nThe d-format (for integers)'
print '\n%md means allocate m spaces overall.'
print 'The number is right-justified within the space allocated.\n\n'
print 'x = %10d' %x
print 'x = %13d' %x
print 'x = %16d' %x

print '\n%-md means allocate m spaces overall.'
print 'The number is left-justified within the space allocated.\n\n'
print 'x = %-10d' %x
print 'x = %-13d' %x
print 'x = %-16d' %x

# The s-format
x = 'quick'
print '\n%s is used for strings'
print 'The %s brown fox is %s.' % (x,x)
print '%10s' % 'the'
print '%10s' % x
print '%10s' %('the ' + x)

