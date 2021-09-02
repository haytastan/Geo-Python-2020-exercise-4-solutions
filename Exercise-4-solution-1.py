# Hayati TAŞTAN
# 02.09.2021
# ===================
# SUBJECT: Simple temperature calculator 
# PROBLEM: https://github.com/haytastan/Geo-Python-2020-exercise-3-solutions/blob/main/Exercise-4-problem-1.ipynb
# SOLUTION: 

# P.A.: pip install nose.tools

from nose.tools import ok_, assert_equal
import inspect

def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * (5/9)




# Check that the function has a single parameter and the parameter name is correct
params = list(inspect.signature(fahr_to_celsius).parameters.keys())

if ok_(params[0]=='temp_fahrenheit') and ok_(len(params)==1):
    print('The function\'s arameter name is incorrect and the function has not a single parameter')
else:
     print('The function\'s arameter name is correct and the function has a single parameter')
        
# 1. What is 48° Fahrenheit in Celsius? 
print('48 degrees Fahrenheit in Celsius is {0:.2f}'.format(fahr_to_celsius(48)))

# 2. What about 71° Fahrenheit in Celsius?
print('71 degrees Fahrenheit in Celsius is {0:.2f}'.format(fahr_to_celsius(71)))


