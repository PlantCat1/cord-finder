#if OMs are already known
import math

planet = input(
"""What planet or moon are you on?
1. Hurston
> """)

if planet == "1":
    global diameter
    diameter = 1000
    global omheight
    omheight = 213.5

OM1Distance = float(input("What is your distance to OM1? > "))
OM2Distance = float(input("What is your distance to OM2? > "))

cord = round(math.sqrt((OM1Distance ** 2) - omheight ** 2), 2)
cord2 = round(math.sqrt((OM2Distance ** 2) - omheight ** 2), 2)
cord2 = abs(cord2 - diameter)

if round(cord, 1) == round(cord2, 1):
    print("Cordinate: " + str(cord))
else:
    print("Please try again.")
    print("Cordinate: " + str(cord))
    print("Cordinate2: " + str(cord2))