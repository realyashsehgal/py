import time
# # #while loops hehe
# # print("Imma make you type your name bet ?")
# # name = ""
# #so wait i can also use not int this like 
# # while len(name) == 0:
# #     name = input("write your name ")
# # while not(name):
# #     name = input("write your name ")
# # print("seee i made you do it huh your name is ew "+name)
# print("Okay so lemme print a table using while loop so answer these questions")
# i = 1
# print("please enter the number of which table you want to print")
# n = int(input("Please enter the number dude"))
# while i<=10:
#     print(i*n)
#     i+=1
# print("so thats it")









#for loop
print("I am using for loop to print 10 digits")
#here in this loop i is decalred right there and range is till 10 it automatically starts from 0
for i in range(10):
    print(i+1)
print("Now i will decide where it should start from")
for i  in range(50,69):
    print(i)
print("I can also iterate throught a string one by one like this")
name = "Mugiwara no luffy"
for i in  name:
    print(i)
print("Now i am making a countdown lets see")
for num in range(10,0,-1):
    print(num)
    time.sleep(1)
print("ggs")