# WindChill.py
# Charles Van Loan
# January 1, 2015
""" Windchill is a function of temperature and wind.

Solicits temperature and wind via
input and then displays the associated windchill
temperature."""


Temp = input('Enter a temperature <= 50F :  ')
Wind = input('Enter a wind speed  >= 3mph:  ')
# Model parameters
A = 35.74; B = .6215; C = -35.75; D = .4275; e = .16
# Compute and display the associated windchill...
WC = (A+B*Temp) + (C+D*Temp)*Wind**e
print Temp,WC
print '                 Windchill :%4.0f' % WC






