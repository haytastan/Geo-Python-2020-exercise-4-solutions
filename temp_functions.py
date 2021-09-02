def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * (5/9)

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
