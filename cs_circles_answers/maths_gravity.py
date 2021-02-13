""" This program inputs a positive-float number and calculates time based on the given equation."""
# evaluate the quadratic formula for calculating time.
#t =( v - (v2 -4(-4.9)(11000))* 0.5)/2(-4.9)
velocity = float(input())
time_taken = ( velocity - ((velocity * velocity) -(4 * (-4.9) * 11000))**0.5 ) / (2 *(-4.9))
print(time_taken)
