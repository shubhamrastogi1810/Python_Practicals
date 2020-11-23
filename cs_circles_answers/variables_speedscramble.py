"""input the total distance and time,calculates average speed and prints it. """
uphill_distance = int(input("Enter uphill Distance."))
downhill_distance = int(input("Enter downhill Distance."))
uphill_time = int(input("Enter uphill time to go."))
downhill_time = int(input("Enter downhill time to go."))

total_distance = uphill_distance + downhill_distance
total_time = uphill_time + downhill_time
average_speed = total_distance / total_time
print(average_speed)
