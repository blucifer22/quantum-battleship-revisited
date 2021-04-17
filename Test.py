from enum import Enum
import qiskit
from qiskit import QuantumCircuit, execute, Aer
import os
import random
import time

# the current player (either 0 or 1)
Player = 0

# initialize randomizer seed
random.seed(time.monotonic())

# initialize ship health (will change when quantum circuits are implemented)
Ship1Health = [0,0,0,0,0]
Ship2Health = [0,0,0,0,0]

# can change the turns later if needed
maxTurns = 4
# turn iterator
turn = 0

# initialize quantum circuits for use in each round
healthQCsArray = []

for i in range(0,maxTurns):
    healthQCsArray.append(QuantumCircuit(10,10))

# initialize backend
backend = Aer.get_backend('qasm_simulator')

class Board:
    
    boardArt = ""
    isHit = []
    mapPos = []

    def __init__(self):
        self.boardArt = "1o----2o\n |\   /|\n | \ / |\n | 3o  |\n | / \ |\n |/   \|\n4o----5o"
        self.isHit = [False, False, False, False, False]
        self.mapPos = [0,0,0,0,0]
    
    def DrawBoard(self):
         print(self.boardArt)

    def HideShip(self, locationRequest):
        location = int(locationRequest) - 1
        self.mapPos[location] = 1
    
    # really bad way of changing characters, can change later
    def ChangeBoard(self, locationStr):
        boardArtList = list(self.boardArt)

        location = int(locationStr)

        if self.isHit[location - 1] == False:
            self.isHit[location - 1] = True
            if location == 1:
                boardArtList[1] = "x"
            elif location == 2:
                boardArtList[7] = "x"
            elif location == 3:
                boardArtList[31] = "x"
            elif location == 4:
                boardArtList[55] = "x"
            elif location == 5:
                boardArtList[len(boardArtList) - 1] = "x"
        
        self.boardArt = "".join(boardArtList)

def SwitchPlayer(player):
    if player == 0:
        return 1
    else:
        return 0


def getHealth(qcResults):
    memory = results.data()
    hexDeci = memory['counts']
    for key, value in hexDeci.items():
        testHex = key
    
    hexAsInt = int(testHex, 16)
    hexAsBin = bin(hexAsInt)
    trueBin = hexAsBin[2:]
    largestIndex = len(trueBin)

    shipHealth = [0,0,0,0,0,0,0,0,0,0]

    for i in range(0,largestIndex):
        shipHealth[i] = int(trueBin[largestIndex - 1 - i])

    return shipHealth


# initialize boards
board1 = Board()
board2 = Board()

# initializing weapon

# initialize hiding checkers
isHiddenP1 = False
isHiddenP2 = False

# Ship hidding phase
os.system("clear")

while isHiddenP1 == False:
    board1.DrawBoard()
    print("Player one, hide your ship")
    hideLocation = input("Choose location to hide: ")

    if hideLocation.isnumeric():
        if int(hideLocation) < 5:
            board1.HideShip(hideLocation)
            isHiddenP1 = True
        else:
            os.system("clear")
            print("Invalid selection. Selection must be between 1 and 5")
    else:
        os.system("clear")
        print("You must provide a numeric position")

os.system("clear")
board2.DrawBoard()

while isHiddenP2 == False:
    print("Player two, hide your ship")
    hideLocation = input("Choose location to hide: ")

    if hideLocation.isnumeric():
        if int(hideLocation) < 5:
            board1.HideShip(hideLocation)
            isHiddenP2 = True
        else:
            os.system("clear")
            print("Invalid selection. Selection must be between 1 and 5")
    else:
        os.system("clear")
        print("You must provide a numeric position")

# main game loop
while turn < maxTurns:

    # update ship health
    j = 0
    for i in Ship1Health:
        if i == 1:
            healthQCsArray[turn].x(j)
        
        j += 1

    for k in Ship2Health:
        if i == 1:
            healthQCsArray[turn].x(j)

        j += 1

    # initialize input checks
    hasChosenShotLocationP1 = False
    hasChosenShotLocationP2 = False

    hasChosenWeaponP1 = False
    hasChosenWeaponP2 = False

    os.system("clear")
    print("Current player: " + str(Player))

    while hasChosenShotLocationP1 == False:
        board2.DrawBoard()
        shotLocation = input("Choose a location to strike: ")

        # check if input is valid
        if shotLocation.isnumeric:
            if int(shotLocation) <= 5:
                hasChosenShotLocationP1 = True
            else:
                os.system("clear")
                print("Invalid selection. Selection must be between 1 and 5")
        else:
            os.system("clear")
            print("Must give numeric selection")

    while hasChosenWeaponP1 == False:
        weaponChoice = input("Choose your weapon (weapons: Shell, Jammer, Health_Steal): ")

        #check if input is valid
        if weaponChoice.lower() == "shell":
            hasChosenWeaponP1 = True
        elif weaponChoice.lower() == "jammer":
            hasChosenWeaponP1 = True
        elif weaponChoice.lower() == "health_steal":
            hasChosenWeaponP1 = True
        else:
            print("Must choose a valid weapon")

    board2.ChangeBoard(shotLocation)

    if board2.mapPos[int(shotLocation) - 1] == 1:
        # Player 2's ship health qubits are 5-9
        shipSectionHit = random.randint(5, 9)

        if weaponChoice == "shell":
            healthQCsArray[turn].x(shipSectionHit)
        elif weaponChoice == "jammer":
            healthQCsArray[turn].h(shipSectionHit)
        elif weaponChoice == "health_steal":
            # TODO implement health steal using teleportation
            healthQCsArray[turn].x(shipSectionHit)
    else:
        print("Target missed")

    Player = SwitchPlayer(Player)

    os.system("clear")
    print("Current player: " + str(Player))

    while hasChosenShotLocationP2 == False:
        board1.DrawBoard()
        shotLocation = input("Choose a location to strike: ")

        # check if input is valid
        if shotLocation.isnumeric:
            if int(shotLocation) <= 5:
                hasChosenShotLocationP2 = True
            else:
                os.system("clear")
                print("Invalid selection. Selection must be between 1 and 5")
        else:
            os.system("clear")
            print("Must give numeric selection")

    while hasChosenWeaponP2 == False:
        weaponChoice = input("Choose your weapon (weapons: Shell, Jammer, Health_Steal): ")

        #check if input is valid
        if weaponChoice.lower() == "shell":
            hasChosenWeaponP2 = True
        elif weaponChoice.lower() == "jammer":
            hasChosenWeaponP2 = True
        elif weaponChoice.lower() == "health_steal":
            hasChosenWeaponP2 = True
        else:
            print("Must choose a valid weapon")

    board1.ChangeBoard(shotLocation)

    if board1.mapPos[int(shotLocation) - 1] == 1:
        # Player 1's ship health qubits are 0-4
        shipSectionHit = random.randint(0, 4)

        if weaponChoice == "shell":
            healthQCsArray[turn].x(shipSectionHit)
        elif weaponChoice == "jammer":
            healthQCsArray[turn].h(shipSectionHit)
        elif weaponChoice == "health_steal":
            # TODO implement health steal using teleportation
            healthQCsArray[turn].x(shipSectionHit)
    else:
        print("Target missed")

    
    # Calculate this round's quantum circuit results
    healthQCsArray[turn].measure(range(0,10),range(0,10))

    endRoundResults = execute(healthQCsArray[turn], backend=backend, shots=1).result()

    endRoundHealth = getHealth(endRoundResults)

    Ship1Health = endRoundHealth[0:5]
    Ship2Health = endRoundHealth[5:10]

    Player = SwitchPlayer(Player)

    turn += 1

print(Ship1Health)
print(Ship2Health)
