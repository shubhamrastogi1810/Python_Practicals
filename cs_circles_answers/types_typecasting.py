"""This program will input pizza length calculates its area and prints person feeded with it."""
# Here we assume that each person eats 100 cm2 pizza.
# Example: if inputStr is "17.5", the area will be 306.25 cm2, so 3 is the correct output.
input_str = float(input("inputStr"))
length = float(input_str)
area = length * length
person_to_feed  = area // 100
print(person_to_feed)
