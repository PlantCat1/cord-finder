import math

def omfinder():
    cord = float(input("Cord: "))
    OM1Leg = cord
    OM2Leg = diameter - cord
    print("OM1 Leg Distance: " + str(OM1Leg))
    print("OM2 Leg Distance: " + str(OM2Leg))
    OM1Distance = round(math.sqrt((OM1Leg ** 2) + omheight ** 2), 2)
    OM2Distance = round(math.sqrt((OM2Leg ** 2) + omheight ** 2), 2)
    print("Distance to OM1: " + str(OM1Distance))
    print("Distance to OM2: " + str(OM2Distance))

def cordfinder():
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

omorcord = input("From OMs or from cords? (1/2) ")

if omorcord == "1":
    omorcord = True
elif omorcord == "2":
    omorcord = False
else:
    print("Please type either 1 or 2.")
    quit()

planet = input(
"""What planet or moon are you on?
1. Hurston
> """)

if planet == "1":
    global diameter
    diameter = 1000
    global omheight
    omheight = 213.5

if omorcord == True:
    omfinder()
else:
    cordfinder()