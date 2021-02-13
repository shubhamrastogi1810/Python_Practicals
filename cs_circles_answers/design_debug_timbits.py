"""This program will arrange the remaining timbits in minimum boxes and calculates its cost."""
# we have to find the total cost the timbits we want
# timbits cost table
#     Number               Price

#       1                  $0.20
#      10 (small box)      $1.99
#      20 (medium box)     $3.39
#      40 (large box)      $6.19
timbits = int(input())
TOTAL = 0

big_box = timbits // 40
TOTAL += big_box*6.19
timbits -= 40*big_box

med_box =  timbits // 20
TOTAL += med_box*3.39
timbits -= 20 * med_box

small_box = timbits // 10
TOTAL += small_box * 1.99
timbits -= 10 * small_box

TOTAL += timbits*0.20

print(TOTAL)
