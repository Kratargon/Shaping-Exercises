# A game of Battleship

class Board:
    def __init__(self, size, ships):
        # Expecting a tuple/array containing two elements; x and y axis
        self.xLength = size[0]
        self.yLength = size[1]
        # Expecting a list of Ship objects
        self.ships = ships
        self.map = []
        # Column-array format so we index by [x][y]
        for i in range(self.xLength):
            column = []
            for j in range(self.yLength):
                # 0 denotes an empty location on the board
                # 1 denotes a location containing a ship
                # 2 denotes a miss
                # 3 denotes a hit
                column.append(0)
            self.map.append(column)

    def placeShip(self, ship, start, direction):
        # Expecting ship to be an element of self.ships
        if ship not in self.ships:
            print("You don't have this ship!")
            return
        # Expecting start to be a coordinate pair within the board
        if 0 > start[0] or self.xLength < start[0] or 0 > start[1] or self.yLength < start[1]:
            print("This isn't a valid board location!")
            return
        # Expecting the ship to not fall off the board

        # Expecting the ship to not overlap with another ship

    def printBoard(self, skin = "default"):
        return ""

class Ship:
    def __init__(self, size):
        # The length of the ship
        self.size = size
        # The direction the ship is pointing (up, right, down, left) -> inits to Right
        self.direction = 1
        # The location of the ship's origin -> inits to under the board
        self.location = [0, -1]