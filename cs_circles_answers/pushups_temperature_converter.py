""" This program will convert Fahrenheit values to celsius and vice-versa."""
# Fahrenheit to Celsius formula ->  f = c * 9/5 + 32
# Celsius to Fahrenheit formula ->  c = (f - 32)*5/9
# Sample input:-  1) 8F :- "-13.333C" 2) "12.5C" :- 54.5F
value = input("Enter the temperature.")
temp_value = float(value[0:-1])
if value[-1] == "c" or value[-1] == "C":
    fahrenheit = temp_value * 9 /5 + 32
    print(str(fahrenheit)+"F")
elif value[-1] == "f" or value[-1] == "F":
    celsius = (temp_value - 32)* 5/9
    print(str(celsius)+"C")
else:
    print("Invalid Values entered other than F and C.")
