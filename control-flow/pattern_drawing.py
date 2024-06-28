integer = int(input("Enter the size of the pattern: "))
x = 0
while x <= integer:
    y = 0;
    for y in range(1, integer + 1):
        print ("*", end="")
        y = y + 1
    x = x + 1     
    print()