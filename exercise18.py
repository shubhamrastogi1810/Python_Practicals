def total(numbers):
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

print(total([1, 2, 3]))
print(total([7, -4, 1, 6, 0]))
print(total([]))



def product(numbers):
    total_so_far = 1
    for number in numbers:
        total_so_far *= number
    return total_so_far



print(product([1, 2, 3]))
print(product([7, -4, 1, 6, 0]))
print(product([]))

