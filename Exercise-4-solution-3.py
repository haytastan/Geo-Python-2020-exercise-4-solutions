# Hayati TAŞTAN
# 02.09.2021
# ===================
# SUBJECT: Applying the classifier 
# PROBLEM: https://github.com/haytastan/Geo-Python-2020-exercise-4-solutions/blob/main/Exercise-4-problem-3.ipynb
# SOLUTION:  

# P.A.: pip install nose.tools

from nose.tools import ok_, assert_equal
import inspect

from temp_functions import fahr_to_celsius, temp_classifier

temp_classes = []

# List of half-hourly temperature values (in degrees Fahrenheit) for one week
temp_data =  [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 
              34, 34, 34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27,
              27, 27, 23, 23, 21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 
              39, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30,
              28, 27, 27, 25, 23, 23, 21, 21, 19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 
              37, 39, 39, 39, 39, 41, 41, 39, 39, 39, 39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28,
              27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21, 19, 21, 19, 21, 21, 19, 21, 27, 28, 32,
              36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41, 41, 41, 41, 39, 37, 36, 36, 34,
              32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19, 19, 19, 19, 19, 21, 23,
              23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43, 43, 43, 43, 43,
              43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28, 28, 27,
              27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
              37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19,
              19, 19, 18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34,
              36, 36, 36, 36, 36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30,
              30, 30, 30, 30, 28, 28]

for i in range(len(temp_data)):
    temp_celcius = fahr_to_celsius(temp_data[i])
    temp_class = temp_classifier(temp_celcius)
    temp_classes.append(temp_class)
    
zeros = temp_classes.count(0)
ones = temp_classes.count(1)
twos = temp_classes.count(2)
threes = temp_classes.count(3)
               

# 1. How many 0 values exist in temp_classes -list?
print("temp_classes -list contains {count: .0f} 0 values".format(count=zeros))

# 2. How many 1 values exist in temp_classes -list?
print("temp_classes -list contains {count: .0f} 1 values".format(count=ones))

# 3. How many 2 values exist in temp_classes -list?
print("temp_classes -list contains {count: .0f} 2 values".format(count=twos))

# 4. How many 3 values exist in temp_classes -list?
print("temp_classes -list contains {count: .0f} 3 values".format(count=threes))

# Check that the functions have a single parameter
t_params = list(inspect.signature(temp_classifier).parameters.keys())
f_params = list(inspect.signature(fahr_to_celsius).parameters.keys())

if ok_(len(t_params)==1) and ok_(len(f_params)==1):
    print('The functions have not a single parameter')
else:
     print('The functions have a single parameter')

# Check that functions are in the namespace (in the current directory)
if ok_(inspect.isfunction(fahr_to_celsius)) and ok_(inspect.isfunction(temp_classifier)):
    print('The functions are not in the namespace')
else:
    print('The functions are in the namespace')

# Check that variable has been created
if ok_('temp_celcius' in locals()) and ok_('temp_class' in locals()) and ok_('temp_classes' in locals()):
    print('The variables have not been been created')
else:
    print('The variables have been been created')

# Check that temp_classes is a list
if ok_(type(temp_classes) == list):
    print('The variables have not been been created')
else:
    print('The variables have been been created')

# Check that the variable "zeros" exists and is correct
if ok_('zeros' in locals()):
    print('the variable "zeros" doesn\'t exists or correct')
else:
    print('the variable "zeros" exists and is correct')
    
# Check that the variable "ones" exists and is correct
if ok_('ones' in locals()):
    print('the variable "ones" doesn\'t exists or correct')
else:
    print('the variable "ones" exists and is correct')

# Check that the variable "twos" exists and is correct
if ok_('twos' in locals()):
    print('the variable "twos" doesn\'t exists or correct')
else:
    print('the variable "twos" exists and is correct')

# Check that the variable "threes" exists and is correct
if ok_('threes' in locals()):
    print('the variable "threes" doesn\'t exists or correct')
else:
    print('the variable "threes" exists and is correct')
