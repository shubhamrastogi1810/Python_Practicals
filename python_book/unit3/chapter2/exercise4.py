""" This is a lab exercise of python book Example 4. """
# This example will input a fahrenheit temperature and convert it into celsius.
def convert_temperature(temp_fahren):
    """ This function will convert the temperature from Fahrenheit to Celsius. """
    celsius = (temp_fahren - 32)*5/9
    print(round(celsius,2))

temperature = float(input("Enter the temperature in Fahrenheit."))
convert_temperature(temperature)
