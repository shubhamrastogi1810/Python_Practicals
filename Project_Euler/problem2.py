""" This program will print the sum of even-valued terms upto 4 million of a fibonacci series."""

FIRST = 1
SECOND = 2
EVE_ADD = 2

while FIRST + SECOND <= 4000001:

    ADD = FIRST + SECOND

    if ADD % 2 == 0:
        EVE_ADD+=ADD

    FIRST = SECOND
    SECOND = ADD

print(EVE_ADD)
