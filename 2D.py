"""
parent function for circle: (x - h)^2 + (y - k)^2 = r^2
h = offset from origin in x direction
k = offset from origin in y direction
r = radius
h and k are flipped (- h is offset to the right)
r is sqaured (r of 100 only makes radius of 10)
 1
4*2
 3
"""

import math

omdistance = 10 #OM distances from origin
x = round(float(input("x cord?: ")), 2)
y = round(float(input("y cord?: ")), 2)


om1distance = round(math.sqrt((abs(x) ** 2) + abs(y - omdistance) ** 2), 2) #calculates components of distance to om and then finds hypotunese
om2distance = round(math.sqrt((abs(x - omdistance) ** 2) + abs(y) ** 2), 2)
om3distance = round(math.sqrt((abs(x) ** 2) + abs(y - -omdistance) ** 2), 2)
om4distance = round(math.sqrt((abs(x - -omdistance) ** 2) + abs(y) ** 2), 2)
centerdistance = round(math.sqrt((abs(x) ** 2) + abs(y - omdistance) ** 2), 2)

if centerdistance > omdistance:
    print("\nThis coordinate is not possible given the planet radius")

print(
    "\n"
    f"om1 distance: {om1distance}\n"
    f"om2 distance: {om2distance}\n"
    f"om3 distance: {om3distance}\n"
    f"om4 distance: {om4distance}\n"
)

#print("OM1: " + str(OM1Distance))
#print("OM2: " + str(OM2Distance))
#print("OM3: " + str(OM3Distance))
#print("OM4: " + str(OM4Distance))