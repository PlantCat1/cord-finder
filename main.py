import math

cord = int(input("Cord: "))
OM1Leg = cord
OM2Leg = 4 - cord

print(OM1Leg)
print(OM2Leg)

OM1Distance = round(math.sqrt((OM1Leg ** 2) + 2**2), 2)
print(OM1Distance)