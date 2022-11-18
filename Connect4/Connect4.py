class BGColors:
    CLEAR = "\033[0m"
    RED = "\033[41m"


class FontColors:
    CLEAR = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"


class PlayerManager:
    def __init__(self):
        r = FontColors.RED + "R" + FontColors.CLEAR
        g = FontColors.GREEN + "G" + FontColors.CLEAR
        self.players = [r, g]
        self.currentPlayer = self.players[0]

    def togglePlayer(self):
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
        else:
            self.currentPlayer = self.players[0]


class Grid:
    def __init__(self):
        self.grid = []
        self.lines = 7
        self.columns = 8
        self.FV = "◊"  # Free Value
        self.reset()

    def reset(self):
        #[
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #    [FV, FV, FV, FV, FV, FV, FV, FV],
        #]
        for line in range(self.lines):
            self.grid.append([])
            for col in range(self.columns):
                self.grid[line].append(self.FV)

        # ----- Debug ----
        #self.grid = [["A1", "F1", "K1", "P1", "U1", "A2", "F2", "K2"],
        #             ["B1", "G1", "L1", "Q1", "V1", "B2", "G2", "L2"],
        #             ["C1", "H1", "M1", "R1", "X1", "C2", "H2", "M2"],
        #             ["D1", "I1", "N1", "S1", "Z1", "D2", "I2", "N2"],
        #             ["E1", "J1", "O1", "T1", "#1", "E2", "J2", "O2"]]

    def draw(self):
        print("| ", end="")
        for y in range(len(self.grid[0])):
            print(str(y + 1) + " | ", end="")

        print("")
        print("-" * 33)
        for y in range(len(self.grid)):
            print("| ", end="")
            for x in range(len(self.grid[y])):
                print(self.grid[y][x] + " | ", end="")
            print("")
        print("-" * 33)

    def setCell(self, currentPlayer, y, x):
        self.grid[y][x] = currentPlayer

    def hasWin(self, currentPlayer):
        # Horizontal Check
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y]) - 3):
                if currentPlayer == self.grid[y][x] == self.grid[y][
                        x + 1] == self.grid[y][x + 2] == self.grid[y][x + 3]:
                    return True

        # Vertical Check
        for y in range(len(self.grid) - 3):
            for x in range(len(self.grid[y])):
                if currentPlayer == self.grid[y][x] == self.grid[
                        y + 1][x] == self.grid[y + 2][x] == self.grid[y +
                                                                      3][x]:
                    return True

        # Diagonal - Top-Down
        for y in range(len(self.grid) - 3):
            for x in range(len(self.grid[y]) - 3):
                if currentPlayer == self.grid[y][x] == self.grid[y + 1][
                        x + 1] == self.grid[y + 2][x + 2] == self.grid[y +
                                                                       3][x +
                                                                          3]:
                    return True

        # Diagonal - Down-Top
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y]) - 3):
                if currentPlayer == self.grid[y][x] == self.grid[y - 1][
                        x + 1] == self.grid[y - 2][x + 2] == self.grid[y -
                                                                       3][x +
                                                                          3]:
                    return True

        return False


class Game:
    def __init__(self):
        self.players = PlayerManager()
        self.grid = Grid()

        print("-" * 25)
        print("--- Let's play a Game ---")
        print("------- Connect 4 -------")
        print("-" * 25)

        hasWin = False
        while not hasWin:
            self.grid.draw()  # Print the current board
            isValidMove = self.playerLine()  # Play
            hasWin = self.grid.hasWin(self.players.currentPlayer)  # Check Win
            if isValidMove: self.players.togglePlayer()  # Change Player
            else: print(BGColors.RED + "Invalid move!" + BGColors.CLEAR)

    def playerLine(self):
        currentPlayer = self.players.currentPlayer
        line = int(input(currentPlayer + ": ")) - 1

        for y in range(len(self.grid.grid) - 1, -1, -1):
            cell = self.grid.grid[y][line]
            if cell == self.grid.FV:
                self.grid.setCell(currentPlayer, y, line)
                return True

        return False


if __name__ == "__main__":
    Game()
