x = int(input("number of index"))

arr = [0] *x
for i in range (x):
    # arr = int(input("enter the value of index"))
    print("enter the value of index " ,i)
    arr[i] = int(input())
   
for i in range (0,x) :
    print(arr[i],end=" ")
print("enter the number you want to remove ")
y = int(input())
for i in range (0,x):
    if(arr[i] == y) :
        print("-")
    print(arr[i])

