""" calcualte the time from the equation """
#-4.9t2 - vt + 11000,
# evaluate the quadratic formula
#t =( v - (v2 -4(-4.9)(11000))* 0.5)/2(-4.9)
velocity = float(input())
time_taken = ( velocity - ((velocity * velocity) -(4 * (-4.9) * 11000))**0.5 ) / (2 *(-4.9))
print(time_taken)
