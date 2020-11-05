frmt = '{:18}:{:.2f}'
distance = int(input("Enter the distance in KMs"))
meters = distance * 1000
feet = distance * 3280.83
inch = distance * 39370.07
cm = distance * 100000
print(frmt.format("meters",meters))
print(frmt.format("feet",feet))
print(frmt.format("inch",inch))
print(frmt.format("centimeters",cm))
