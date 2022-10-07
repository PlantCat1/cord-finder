"""
parent function for circle: (x - h)^2 + (y - k)^2 = r^2
h = offset from origin in x direction
k = offset from origin in y direction
r = radius
h and k are flipped (- h is offset to the right)
r is sqaured (r of 100 only makes radius of 10)
change in x = x2 - x1
change in y = y2 - y1
distance = (x^2 + y^2)^.5
distance = ((x2 - x1)^2 + (y2 - x1)^2)^.5
 1
4*2
 3
"""

import math

omdistance = 10 #OM distances from origin
bodyradius = 5 #radius of planet

devmode = input("devmode 'on' or 'off'?: ")
if devmode == "on":
    devmode = True
else:
    devmode = False

if devmode == True:
    print("devmode is now enabled.")

def omfinder():
    x = round(float(input("x cord?: ")), 2)
    y = round(float(input("y cord?: ")), 2)
    om1distance = round(math.sqrt((abs(x) ** 2) + abs(y - omdistance) ** 2), 2) #calculates components of distance to om and then finds hypotunese
    om2distance = round(math.sqrt((abs(x - omdistance) ** 2) + abs(y) ** 2), 2)
    om3distance = round(math.sqrt((abs(x) ** 2) + abs(y - -omdistance) ** 2), 2)
    om4distance = round(math.sqrt((abs(x - -omdistance) ** 2) + abs(y) ** 2), 2)
    centerdistance = round(math.sqrt(abs(x) ** 2 + abs(y) ** 2), 2)
    if centerdistance > bodyradius:
        print("\nThese coordinates are not possible given the planet radius")
    print(
        f"OM1 distance: {om1distance}\n"
        f"OM2 distance: {om2distance}\n"
        f"OM3 distance: {om3distance}\n"
        f"OM4 distance: {om4distance}\n"
        f"Center distance: {centerdistance}"
    )

def cordfinder():
    om1distance = round(float(input("OM1 distance?: ")), 2)
    om2distance = round(float(input("OM2 distance?: ")), 2)
    om3distance = round(float(input("OM3 distance?: ")), 2)
    om4distance = round(float(input("OM4 distance?: ")), 2)

omfinderorcordfinder = input("From current cordinates [1] or from OM distances [2]? ")
if omfinderorcordfinder == "1":
    omfinder()
elif omfinderorcordfinder == "2":
    cordfinder()
else:
   print("Enter 1 or 2.")
   quit
