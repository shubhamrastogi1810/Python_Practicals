""" This program will input population of any 5 years and prints them on screen."""
population_info = {}
FRMT = '{:6} : {:}'
filevar = open("population_read.txt","r")
for i in range(5):
    year,population = filevar.readline().split(",")
    population_info[year] = population
print("\n Population Info.")
for key in population_info:
    print(FRMT.format(key,population_info[key]),end='')
