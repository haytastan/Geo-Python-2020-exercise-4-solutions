def hello(name, age):
    return 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'

output = hello(name='Hayati TAŞTAN', age=35)
print(output)


def celsius_to_fahr(temp):
    return 9/5 * temp + 32

def kelvins_to_celsius(temp_kelvins):
    return temp_kelvins - 273.15

freezing_point =  celsius_to_fahr(0)
print('The freezing point of water in Fahrenheit is:', freezing_point)

print('The boiling point of water in Fahrenheit is:', celsius_to_fahr(100))

absolute_zero = kelvins_to_celsius(temp_kelvins=0)
print('Absolute zero in Celsius is:', absolute_zero)


def kelvins_to_fahr(temp_kelvins):
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr

absolute_zero_fahr = kelvins_to_fahr(temp_kelvins=0)

print('Absolute zero in Fahrenheit is:', absolute_zero_fahr)