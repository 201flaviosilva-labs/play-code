print("-- Multiplication Table --")

newNumber = "Y"

while newNumber == "Y":
    print("-"*20)
    num = int(input("Number ➜ "))
    for x in range(11):
        print(f"{x} * {num} = {x * num}")

    newNumber = input("New number [Y/N]: ")
