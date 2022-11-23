import random


class FontColors:
    CLEAR = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"


wordsList = ["apple", "banana", "cherry", "beep", "boop", "dog", "cat"]


class Hangman:
    def __init__(self):
        self.numFailAttempts = 0
        self.selectedLetters = []
        self.currentWord = ""

        playAgain = True
        while playAgain:
          self.start()

          print("Do you want to play again?")
          playAgain = input("[Y/N]: ").upper() == "Y"

    def start(self):
        self.numFailAttempts = 0
        self.selectedLetters = []
        self.currentWord = random.choice(wordsList)
        #print(self.currentWord)
        self.draw()
        self.update()

    def update(self):
        while self.numFailAttempts < 6:
            guess = input("Letter: ")

            if guess in self.selectedLetters:
                print(
                    "Letter already selected")  # User select a repeated letter
            else:
                if guess not in self.currentWord:
                    self.numFailAttempts += 1  # Add one attemp if the user letter are not in the word
                self.selectedLetters.append(guess)
                self.draw()
              
            if self.checkWin():
                print("Nice 👍")
                return
              
        # Game Over      
        print("GAME OVER")
  
    def checkWin(self):
        dashWord = ""
        for i in range(len(self.currentWord)):
            if self.currentWord[i] not in self.selectedLetters:
                dashWord += "_"
        return "_" not in dashWord

    def draw(self):
        # Hiden word
        for i in range(len(self.currentWord)):
            if self.currentWord[i] in self.selectedLetters:
                print(self.currentWord[i], end=" ")
            else:
                print("_", end=" ")
        print("")

        # Selected Letters
        for i in range(len(self.selectedLetters)):
            letter = self.selectedLetters[i]
            letter = (FontColors.GREEN if letter in self.currentWord else
                      FontColors.RED) + letter + FontColors.CLEAR
            print(letter, end=" ")
        print("")

        # Gallows
        if self.numFailAttempts == 0:
            print("________ ")
            print("|      | ")
            print("|        ")
            print("|        ")
            print("|        ")
            print("|        ")

        elif self.numFailAttempts == 1:
            print("________ ")
            print("|      | ")
            print("|      O ")
            print("|        ")
            print("|        ")
            print("|        ")

        elif self.numFailAttempts == 2:
            print("________ ")
            print("|      | ")
            print("|      O ")
            print("|     /  ")
            print("|        ")
            print("|        ")

        elif self.numFailAttempts == 3:
            print("________ ")
            print("|      | ")
            print("|      O ")
            print("|     /| ")
            print("|        ")
            print("|        ")

        elif self.numFailAttempts == 4:
            print("________ ")
            print("|      | ")
            print("|      O ")
            print("|     /|\\")
            print("|        ")
            print("|        ")

        elif self.numFailAttempts == 5:
            print("________ ")
            print("|      | ")
            print("|      O ")
            print("|     /|\\")
            print("|     /  ")
            print("|        ")

        else:
            print("________ ")
            print("|      | ")
            print("|      O ")
            print("|     /|\\")
            print("|     / \\")
            print("|        ")


if __name__ == "__main__":
    Hangman()
