# print("Okay so lets calculate the factorials hehe")
# def fact(num):
#     sol = 1
#     for i in range(1,num+1):
#         sol *= i
#     return sol
# num = int(input("Please enter a number to calculate the facatorial of"))
# print(fact(num))










#Okay so i am going to use args basically it convert all the passed value during called in to a tuple basically pack them up
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print("i am going to call the sum fucntion and send multiple variable lets see if it works")
print(sum(1,2,3,4,5,6))
print("Ayoooo it worked")
