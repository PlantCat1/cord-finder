import math
a = 500
b = 713.5

cord = float(input("What is your current coordinate? > "))

OM1Angle = abs(cord - 0)
OM1Distance = round(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(OM1Angle))), 2)

OM3Angle = abs(cord - 90)
OM3Distance = round(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(OM3Angle))), 2)

OM2Angle = abs(cord - 180)
OM2Distance = round(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(OM2Angle))), 2)

OM4Angle = abs(cord - 270)
OM4Distance = round(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(OM4Angle))), 2)

print("OM1: " + str(OM1Distance))
print("OM2: " + str(OM2Distance))
print("OM3: " + str(OM3Distance))
print("OM4: " + str(OM4Distance))