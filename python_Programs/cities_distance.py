""" this program finds out the distance of 2 cities in different units. """
FRMT = '{:18}:{:.2f}'
distance = int(input("Enter the distance in KMs"))
meters = distance * 1000
feet = distance * 3280.83
inch = distance * 39370.07
cm = distance * 100000
print(FRMT.format("meters",meters))
print(FRMT.format("feet",feet))
print(FRMT.format("inch",inch))
print(FRMT.format("centimeters",cm))
