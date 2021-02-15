"""This code computes combination formula 'n!/r!*(n-r)!' in a function choose taking 2 arguments"""
# Here choose(n,k) takes 2 integer arguments and n>k>0.
def choose(numbers,patterns):
    """This function takes 2 arguments i.e. numbers and pattern value to compute the formula."""
    diff = numbers - patterns
    num = 1
    new_n = 1
    new_k = 1
    while diff > 1:
        num *= diff
        diff -= 1
    while numbers > 1:
        new_n *= numbers
        numbers -= 1
    while patterns > 1:
        new_k *= patterns
        patterns -= 1
    value = new_n / (num * new_k)
    return value
print(choose(4,2))
