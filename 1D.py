import math

def omfinder(): #finds om distances based on cords
    cord = float(input("Cord: "))
    if cord > diameter or cord < 0: #checks cord that value is possible
        print("This coordinate is not possible given the chosen planet.")
        quit()
    OM1Leg = cord #distance from edge of plane
    OM2Leg = diameter - cord
    print("OM1 Leg Distance: " + str(OM1Leg))
    print("OM2 Leg Distance: " + str(OM2Leg))
    OM1Distance = round(math.sqrt((OM1Leg ** 2) + omheight ** 2), 2) #a^2 + b^2 = c^2 using current distance from edge and om heights
    OM2Distance = round(math.sqrt((OM2Leg ** 2) + omheight ** 2), 2)
    print("Distance to OM1: " + str(OM1Distance))
    print("Distance to OM2: " + str(OM2Distance))

def cordfinder(): #finds current cordinate using om distances
    OM1Distance = float(input("What is your distance to OM1? > "))
    OM2Distance = float(input("What is your distance to OM2? > "))
    cord = round(math.sqrt((OM1Distance ** 2) - omheight ** 2), 2) #c^2 - a^2 = b^2
    cord2 = round(math.sqrt((OM2Distance ** 2) - omheight ** 2), 2) #same thing but with other om distance to double check cord value
    cord2 = abs(cord2 - diameter)
    if round(cord, 1) == round(cord2, 1) and cord < diameter and cord > 0:
        print("Cordinate: " + str(cord))
    else:
        print("These OMs are not possible given the chosen planet.")
        print("Cordinate: " + str(cord))
        print("Cordinate2: " + str(cord2))

omorcord = input("From current cordinates [1] or from OM distances[2]? ") #asks user if they want to find OM distance from current cordinates or vice versa

if omorcord == "1": #to later decide which function to use
    omorcord = True
elif omorcord == "2":
    omorcord = False
else:
    print("Please type either 1 or 2.")
    quit()

planet = input( #asks what body user is on so that omheight and planet diameter can be defined. will later have more planets 
"""What planet or moon are you on?
1. Hurston
> """)

if planet == "1": #sets these values based on the previous input
    global diameter
    diameter = 1000
    global omheight
    omheight = 213.5
else:
    print("Please input number representing a given body.")
    quit()

if omorcord == True: #calls upon which function should be used
    omfinder()
else:
    cordfinder()