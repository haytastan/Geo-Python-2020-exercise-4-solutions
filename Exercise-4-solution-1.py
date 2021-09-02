# Hayati TAŞTAN
# 01.09.2021
# ===================
#SUBJECT: Simple temperature calculator 
# PROBLEM: https://github.com/haytastan/Geo-Python-2020-exercise-3-solutions/blob/main/Exercise-3-problem-1.ipynb
# SOLUTION: 

# pip install nose.tools

from nose.tools import ok_, assert_equal
import inspect

def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * (5/9)

print('32 degrees Fahrenheit in Celsius is: ', fahr_to_celsius(32))


# Check that the function has a single parameter and the parameter name is correct
params = list(inspect.signature(fahr_to_celsius).parameters.keys())

if ok_(params[0]=='temp_fahrenheit') and ok_(len(params)==1):
    print('The function\'s arameter name is incorrect and the function has not a single parameter')
else:
     print('The function\'s arameter name is correct and the function has a single parameter')