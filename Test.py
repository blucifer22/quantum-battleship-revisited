from enum import Enum
import os

# the current player (either 0 or 1)
Player = 0

# initialize ship health (will change when quantum circuits are implemented)
Ship1Health = 200
Ship2Health = 200

# can change the turns later if needed
maxTurns = 4
# turn iterator
turn = 0

class Weapon(Enum):
    turret = 20
    torpedo = 50
    tacticle_nuke = 200

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
        weaponChoice = input("Choose your weapon (weapons: Turret, Torpedo, Tacticle_Nuke): ")

        #check if input is valid
        if weaponChoice.lower() == "turret":
            hasChosenWeaponP1 = True
        elif weaponChoice.lower() == "torpedo":
            hasChosenWeaponP1 = True
        elif weaponChoice.lower() == "tacticle_nuke":
            hasChosenWeaponP1 = True
        else:
            print("Must choose a valid weapon")

    board2.ChangeBoard(shotLocation)

    if board2.mapPos[int(shotLocation) - 1] == 1:
        if weaponChoice == "turret":
            Ship2Health -= Weapon.turret.value
        elif weaponChoice == "torpedo":
            Ship2Health -= Weapon.torpedo.value
        elif weaponChoice == "tacticle_tuke":
            Ship2Health -= Weapon.tacticle_nuke.value
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
        weaponChoice = input("Choose your weapon (weapons: Turret, Torpedo, Tacticle_Nuke): ")

        #check if input is valid
        if weaponChoice.lower() == "turret":
            hasChosenWeaponP2 = True
        elif weaponChoice.lower() == "torpedo":
            hasChosenWeaponP2 = True
        elif weaponChoice.lower() == "tacticle_nuke":
            hasChosenWeaponP2 = True
        else:
            print("Must choose a valid weapon")

    board1.ChangeBoard(shotLocation)

    if board1.mapPos[int(shotLocation) - 1] == 1:
        if weaponChoice == "turret":
            Ship1Health -= Weapon.turret.value
        elif weaponChoice == "torpedo":
            Ship1Health -= Weapon.torpedo.value
        elif weaponChoice == "tacticle_nuke":
            Ship1Health -= Weapon.tacticle_nuke.value
    else:
        print("Target missed")

    Player = SwitchPlayer(Player)

    turn += 1

print(Ship1Health)
print(Ship2Health)
