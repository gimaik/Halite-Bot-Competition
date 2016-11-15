from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("RANDOM_BOT")


def move(location):
    site = gameMap.getSite(location)

    maxCardinalProduction = 999
    minCardinalStrength =999

    for d in CARDINALS:
        neighbour_site = gameMap.getSite(location, d)

        if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
            return Move(location, d)

        if  neighbour_site.production < maxCardinalProduction:
            maxCardinalProduction = neighbour_site.production
            maxCardinalProductionSite = d

        if neighbour_site.strength < minCardinalStrength:
            minCardinalStrength = neighbour_site.strength
            minCardinalStrengthSite = d

    if site.strength > 80:
        return Move(location, randomDirection())

    if site.strength < site.production * 8:
        return Move(location, STILL)
    return Move(location, maxCardinalProductionSite)


def randomDirection():

    u = random.random()
    if u <= 0.20:
        return NORTH
    elif u<= 0.40:
        return SOUTH
    elif u <=0.60:
        return EAST
    elif u <=0.80:
        return WEST
    else:
        return STILL

def randomVertHorz():
    u=random.random()
    if u <= 0.50:
        return NORTH
    else:
        return EAST

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(move(location))
    sendFrame(moves)

