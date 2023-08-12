#print a triangle
rows = 5
#control the number of rows
for i in range(rows +1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()