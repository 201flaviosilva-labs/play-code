# Fibonacci

def fibonacci():
  print("-- Fibonacci --")

  max = 100 # Max number to calculate
  lastNumber = 0 # Temp variable just for store the last number
  currentNumber = 1 # The current number of the sequence

  while currentNumber < max:
    next = currentNumber + lastNumber # Helper variable
    lastNumber = currentNumber
    currentNumber = next
    print("Current number: ", currentNumber)
  
fibonacci()
