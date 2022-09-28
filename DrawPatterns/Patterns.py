print("Patterns")
print()
print("-#-" * 20)
print()

# Triangle 1
def triangle1(lines, columns):
    print(" -- Triangle 1 -- ")
    for i in range(lines):
        for j in range(columns):
            if j < i:
                print(" ", end="")
            else:
                print("X ", end="")
        print("")
    print()

# Triangle 2
def triangle2(lines, columns):
    print(" -- Triangle 2 -- ")
    for i in range(lines):
        for j in range(columns, -1, -1):
            if j > i:
                print(" ", end="")
            else:
                print("X ", end="")
        print("")
    print()

# Triangle 3
def triangle3(lines, columns):
    print(" -- Triangle 3 -- ")
    for i in range(lines):
        for j in range(columns):
            if j > i:
                print(" ", end="")
            else:
                print("X ", end="")
        print("")
    print()

# Triangle 4
def triangle4(lines, columns):
    print(" -- Triangle 4 -- ")
    for i in range(lines, -1, -1):
        for j in range(columns):
            if j >= i:
                print(" ", end="")
            else:
                print("X ", end="")
        print("")
    print()


# Box
def box(lines,columns):
    print(" -- Box -- ")
    for i in range(0, lines + 1):
        for j in range(0, columns + 1):
            if i == 0 or i == lines or j == 0 or j == lines:
                print("X ", end="")
            else:
                print("  ", end="")
        print()
    print()

# Box X
def boxX(lines, columns):
    print(" -- Box X -- ")
    for i in range(0, lines + 1):
        for j in range(0, columns + 1):
            if i == 0 or i == lines or j == 0 or j == lines or i == j or i + j == columns:
                print("X ", end="")
            else:
                print("  ", end="")
        print()
    print()

triangle1(10, 10)
triangle2(10, 10)
triangle3(10, 100)
triangle4(10, 10)

box(4, 4)
boxX(10, 10)
