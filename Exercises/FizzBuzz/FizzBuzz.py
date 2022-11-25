# Fizz Buzz
print("-- Fizz Buzz --")

userNumber = int(input("Number: "))

output = ""

if userNumber % 3 == 0:
	output += "Fizz"
if userNumber % 5 == 0:
	output += "Buzz"

if output == "":
	output = userNumber

print(output)
