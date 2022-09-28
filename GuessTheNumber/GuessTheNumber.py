from random import randint

print("------------------------------------------")
print("------------ Lets play a game ------------")
print("------------------------------------------")
print("------------ Guess The Number ------------")
print("------------------------------------------")
print("")

numberOfAttempts = 0
numberMaxOfAttempts = 0
r = "Y"

while r.upper() == "Y":
    print("The hidden number is between 1 and 100")
    numberOfAttempts = 0
    numberMaxOfAttempts = int(input("Select the maximum number of attempts: "))

    rdn = randint(1, 100)
    #print("Hidden number: ", aleatorio)

    for i in range(numberMaxOfAttempts):
        print("")
        numberOfAttempts = numberOfAttempts + 1

        Tentativa = int(input("Number: "))
        print("------------------------------------------")

        if (Tentativa > 100):
            print("")
            print("Error: Number greater than Allowed")
        elif (Tentativa < 0):
            print("")
            print("Error: Number less than Allowed")
        elif (Tentativa > rdn):
            print("")
            print("You number it's too BIG!")
        elif (Tentativa < rdn):
            print("")
            print("You number it's too LOW!")
        else:
            print("")
            print("Right attempt!")
            print("")
            print("Attempts used: ", numberOfAttempts)
            break

        if (numberOfAttempts < numberMaxOfAttempts):
            print("")
            print("Attempts used: ", numberOfAttempts, " you still have: ",
                  numberMaxOfAttempts - numberOfAttempts)
            print("")
            print("------------------------------------------")
            print("")
        else:
            print("")
            print("You've reached the limit of attempts!")
            print("")
            print("------------------------------------------")
            print("")

    print("The hidden number was: ", rdn)
    print("")
    print("------------------------------------------")

    r = input("Play again [Y/N]? ")
    print("")
    print("------------------------------------------")
    print("")

print("The game it's over!")
