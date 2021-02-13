"""This code will input Uphill & Downhill distance and time, and calculates average speed"""
uphill_distance = int(input("Enter uphill Distance."))
downhill_distance = int(input("Enter downhill Distance."))
uphill_time = int(input("Enter uphill time to go."))
downhill_time = int(input("Enter downhill time to go."))

total_distance = uphill_distance + downhill_distance
total_time = uphill_time + downhill_time
average_speed = total_distance / total_time
print(average_speed)
