"""
use python nested loops to print the following pattern:
         *
        **
       ***
     *****
for i in range(1, 5):
    for j in range(1, i + 1):
        if j > i:
            print(" ", end="")
        else:
            print("*", end="") 
    print()
    
rows = 5
for i in range(1, 5):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)
"""

rows = 6
for i in range(rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()