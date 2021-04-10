from enum import Enum

# the current player (either 0 or 1)
Player = 0

# initialize ship health (will change when quantum circuits are implemented)
Ship1Health = 200
Ship2Health = 200

# list to hide ship in
map1 = [0,0,0,0,0]
map2 = [0,0,0,0,0]

# can change the turns later if needed
maxTurns = 4
# turn iterator
turn = 0

class Weapon(Enum):
    Turret = 20
    Torpedo = 50
    Tacticle_Nuke = 200

class Board:
    
    boardArt = ""
    isHit = []

    def __init__(self):
        self.boardArt = "1o----2o\n |\   /|\n | \ / |\n | 3o  |\n | / \ |\n |/   \|\n4o----5o"
        self.isHit = [False, False, False, False, False]
    
    def DrawBoard(self):
         print(self.boardArt)
    
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

# Ship hidding phase
board1.DrawBoard()

print("Player one, hide your ship")
hideLocation = input("Choose location to hide: ")

map1[int(hideLocation) - 1] = 1

board2.DrawBoard()

print("Player two, hide your ship")
hideLocation = input("Choose location to hide: ")

map2[int(hideLocation) - 1] = 1

while(turn < maxTurns):

    board2.DrawBoard()
    print("Current player: " + str(Player))

    shotLocation = input("Choose a location to strike: ")
    weaponChoice = input("Choose your weapon (weapons: Turret, Torpedo, Tacticle_Nuke): ")

    board2.ChangeBoard(shotLocation)

    if map2[int(shotLocation) - 1] == 1:
        if weaponChoice == "Turret":
            Ship2Health -= Weapon.Turret.value
        elif weaponChoice == "Torpedo":
            Ship2Health -= Weapon.Torpedo.value
        elif weaponChoice == "Tacticle_Nuke":
            Ship2Health -= Weapon.Tacticle_Nuke.value
        else:
            print("you've chosen an invalid weapon. No damage dealt")
    else:
        print("Target missed")

    Player = SwitchPlayer(Player)

    board1.DrawBoard()
    print("Current player: " + str(Player))

    shotLocation = input("Choose a location to strike: ")
    weaponChoice = input("Choose your weapon (weapons: Turret, Torpedo, Tacticle_Nuke): ")

    board1.ChangeBoard(shotLocation)

    if map1[int(shotLocation) - 1] == 1:
        if weaponChoice == "Turret":
            Ship1Health -= Weapon.Turret.value
        elif weaponChoice == "Torpedo":
            Ship1Health -= Weapon.Torpedo.value
        elif weaponChoice == "Tacticle_Nuke":
            Ship1Health -= Weapon.Tacticle_Nuke.value
        else:
            print("you've chosen an invalid weapon. No damage dealt")
    else:
        print("Target missed")

    Player = SwitchPlayer(Player)

    turn += 1

print(Ship1Health)
print(Ship2Health)
