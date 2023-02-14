print("ASCII Art")
print()
print("-#-" * 20)
print()

class BGColors:
    CLEAR = "\033[0m"
    RED = "\033[41m"
    GREEN = "\033[42m"

# Triangle 1
def triangle1(lines, columns):
    print(" -- Triangle 1 -- ")
    for i in range(lines):
        for j in range(columns):
            if j < i:
                print(BGColors.RED + " "+ BGColors.CLEAR, end="")
            else:
                print(BGColors.GREEN + "X "+BGColors.CLEAR, end="")
        print("")
    print()

# Triangle 2
def triangle2(lines, columns):
    print(" -- Triangle 2 -- ")
    for i in range(lines):
        for j in range(columns, -1, -1):
            if j > i:
                print(BGColors.RED + " "+ BGColors.CLEAR, end="")
            else:
                print(BGColors.GREEN + "X "+BGColors.CLEAR, end="")
        print("")
    print()

# Triangle 3
def triangle3(lines, columns):
    print(" -- Triangle 3 -- ")
    for i in range(lines):
        for j in range(columns):
            if j > i:
                print(BGColors.RED + "  "+ BGColors.CLEAR, end="")
            else:
                print(BGColors.GREEN + "X "+BGColors.CLEAR, end="")
        print("")
    print()

# Triangle 4
def triangle4(lines, columns):
    print(" -- Triangle 4 -- ")
    for i in range(lines, -1, -1):
        for j in range(columns):
            if j >= i:
                print(BGColors.RED + "  "+ BGColors.CLEAR, end="")
            else:
                print(BGColors.GREEN + "X "+BGColors.CLEAR, end="")
        print("")
    print()


# Box
def box(lines,columns):
    print(" -- Box -- ")
    for i in range(0, lines + 1):
        for j in range(0, columns + 1):
            if i == 0 or i == lines or j == 0 or j == columns:
                print(BGColors.GREEN + "X "+BGColors.CLEAR, end="")
            else:
                print(BGColors.RED + "  "+ BGColors.CLEAR, end="")
        print()
    print()

# Box X
def boxX(lines, columns):
    print(" -- Box X -- ")
    for i in range(0, lines + 1):
        for j in range(0, columns + 1):
            if i == 0 or i == lines or j == 0 or j == lines or i == j or i + j == columns:
                print(BGColors.GREEN + "X "+BGColors.CLEAR, end="")
            else:
                print(BGColors.RED + "  "+ BGColors.CLEAR, end="")
        print()
    print()

# Chess
def chess(width=8, height=8):
    print(" -- Chess -- ")
    RED = BGColors.RED + " X " + BGColors.CLEAR
    GREEN =  BGColors.GREEN + " O " + BGColors.CLEAR
  	
    for x in range(width):
      for y in range(height):
        color = RED if (x + y) % 2 == 0 else GREEN
        print(color, end="")
      print()

triangle1(10, 10)
triangle2(10, 10)
triangle3(10, 10)
triangle4(10, 10)

box(4, 4)
boxX(10, 10)

chess()
