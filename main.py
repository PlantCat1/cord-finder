import math

cord = float(input("Cord: "))
OM1Leg = cord
OM2Leg = 1000 - cord
# number = total # of cords

print(OM1Leg)
print(OM2Leg)

OM1Distance = round(math.sqrt((OM1Leg ** 2) + 2 ** 2), 2)
OM2Distance = round(math.sqrt((OM2Leg ** 2) + 2 ** 2), 2)
# pythagorean theorem, 3rd number is height, last is for rounding

print("Distance to OM1: " + str(OM1Distance))
print("Distance to OM2: " + str(OM2Distance)) 