""" This program will input a fahrenheit temperature and converts it into celsius."""
# This example will input a fahrenheit temperature and convert it into celsius.
def convert_temperature(temp_fahren):
    """ This function converts the temperature from Fahrenheit to Celsius. """
    celsius = (temp_fahren - 32)*5/9
    print(round(celsius,2))

temperature = float(input("Enter the temperature in Fahrenheit."))
convert_temperature(temperature)
