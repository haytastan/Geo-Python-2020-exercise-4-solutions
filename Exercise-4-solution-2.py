# Hayati TAŞTAN
# 02.09.2021
# ===================
# SUBJECT: Temperature classifier 
# PROBLEM: https://github.com/haytastan/Geo-Python-2020-exercise-4-solutions/blob/main/Exercise-4-problem-2.ipynb
# SOLUTION: 

# P.A.: pip install nose.tools

from nose.tools import ok_, assert_equal
import inspect

def temp_classifier(temp_celsius):
    
    if (temp_celsius < -2):
        category = 0
    elif (temp_celsius <= -2 or temp_celsius < 2):
        category = 1
    elif (temp_celsius <= 2 or temp_celsius < 15):
        category = 2
    else:
        category = 3
       
    return (category)

# Check that the function has a single parameter and the parameter name is correct
params = list(inspect.signature(temp_classifier).parameters.keys())

if ok_(params[0]=='temp_celsius') and ok_(len(params)==1):
    print('The function\'s parameter name is incorrect and the function has not a single parameter')
else:
     print('The function\'s parameter name is correct and the function has a single parameter')


# 1. What is the class value for 16.5 degrees (Celsius)?
print('16.5 degrees (Celsius) is in class {0:.1f}'.format(temp_classifier(16.5)))

# 2. What is the class value for +2 degrees (Celsius)?
print('+2 degrees (Celsius) is in class {0:.1f}'.format(temp_classifier(2))) 

