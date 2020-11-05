numbers = [5,7,11,13,17,19,29,31]

numbers[1]=3
print(numbers)
del(numbers[3])
print(numbers)
numbers[3]=37
print(numbers)
numbers[4]= numbers[5]
print(numbers)
numbers.append(37)
print(numbers)
numbers.remove(29)
print(numbers)
numbers.insert(3,13)
print(numbers)