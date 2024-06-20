print("hehe i am printing a triangle patter")
print("Please enter the number of rows you want in it")
rows = int(input())
for i in range (1 , rows):
    for j in range ( i, rows):
        print(" ",end="");
    for j in range( i ):
        print("*", end="");
    for j in range( i-1 ):
        print("*", end="");
    print()
for i in range(1,rows+1):
    for j in range( i-1 ):
        print(" ", end="");
    for j in range ( i, rows):
        print("*",end="");
    for j in range ( i-1, rows):
        print("*",end="");
    print()