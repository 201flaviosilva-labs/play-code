class BGColors:
    CLEAR = "\033[0m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    CYAN = "\033[46m"


class FontColors:
    CLEAR = "\033[0m"
    ORANGE = "\033[33m"
    PURPLE = "\033[35m"


"""
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
"""
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

moves = 0

currentPlayerIndex = 0
players = ["X", "O"]


def reset():
    global board, moves, currentPlayerIndex

    print("-" * 50)
    print("Let's play a Game")
    print("The Tic Tac Toe Game")
    print("-" * 50)

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    moves = 0
    currentPlayerIndex = 0


def getCurrentPlayer():
    return players[currentPlayerIndex]


def togglePlayer():
    global currentPlayerIndex
    if currentPlayerIndex == 0: currentPlayerIndex = 1
    else: currentPlayerIndex = 0


def colorizePlayer(player):
    if player == players[0]:
        return FontColors.PURPLE + player + FontColors.CLEAR
    elif player == players[1]:
        return FontColors.ORANGE + player + FontColors.CLEAR
    else:
        return player

def isValiedPosition(position):
  if position > 9 or position < 1: return False
  elif board[position - 1] == players[0] or board[position - 1] == players[1]: return False

  return True

def printBoard():
    print()
    print("-" * 50)

    print(
        colorizePlayer(board[0]) + " | " + colorizePlayer(board[1]) + " | " +
        colorizePlayer(board[2]))
    print("-" * 9)
    print(
        colorizePlayer(board[3]) + " | " + colorizePlayer(board[4]) + " | " +
        colorizePlayer(board[5]))
    print("-" * 9)
    print(
        colorizePlayer(board[6]) + " | " + colorizePlayer(board[7]) + " | " +
        colorizePlayer(board[8]))

    print("-" * 50)
    print()


def getWinner():
    # Horizontal
    if board[0] == board[1] == board[2]: return board[0]
    elif board[3] == board[4] == board[5]: return board[3]
    elif board[6] == board[7] == board[8]: return board[6]

    # Vertical
    elif board[0] == board[3] == board[6]: return board[0]
    elif board[1] == board[4] == board[7]: return board[1]
    elif board[2] == board[5] == board[8]: return board[2]

    # Diagonal
    elif board[0] == board[4] == board[8]: return board[0]
    elif board[2] == board[4] == board[6]: return board[2]

    # None
    else: False


def newMove():
    global moves

    # Print Board
    printBoard()

    # Get user move
    print("Current player: " + getCurrentPlayer())
    position = int(input("Position [1-9]: ") or 0)

    # Check user move
    if not isValiedPosition(position):
        print(BGColors.RED + "Invalid position!" + BGColors.CLEAR)
        return

    # Update
    moves += 1
    board[position - 1] = getCurrentPlayer()
    togglePlayer()


def game():
    isPlayAgain = True

    while isPlayAgain:
        reset()
        hasNoWinner = True
      
        while moves < 9 and hasNoWinner: # "Update"
            newMove()
            hasNoWinner = not (getWinner() == players[0]
                               or getWinner() == players[1])

        # End Game
        printBoard()
        if getWinner(): print(BGColors.GREEN + "Winner: " + str(getWinner()) + BGColors.CLEAR)
        else: print(BGColors.CYAN + "A Tie!" + BGColors.CLEAR)
        isPlayAgain = input("Want to play again? [Y/N] ").upper() == "Y"

    # No play again
    print("Bye")


if __name__ == "__main__":
    game()
