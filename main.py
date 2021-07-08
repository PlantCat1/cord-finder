#if cord is already known
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

cord = float(input("Cord: "))
OM1Leg = cord
OM2Leg = diameter - cord

print(OM1Leg)
print(OM2Leg)

OM1Distance = round(math.sqrt((OM1Leg ** 2) + omheight ** 2), 2)
OM2Distance = round(math.sqrt((OM2Leg ** 2) + omheight ** 2), 2)

print("Distance to OM1: " + str(OM1Distance))
print("Distance to OM2: " + str(OM2Distance)) 