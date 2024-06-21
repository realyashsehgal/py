# #doing exception handling just watch
# try:
#     x = int(input("Please enter a number "))
#     y = int(input("Please enter a number you want to divide it with"))
#     result = x/y
#     print(result)
# except ZeroDivisionError:
#     print("Bro wtf is wrong with you can you divide anything by zero")
# except ValueError:
#     print("WHAT THE ACTUAL FUCK is wrong with you how can you divide fucking with a number ")
# except Exception:
#     print("Something Went wrong :(")
try:
    x = int(input("Please enter a number "))
    y = int(input("Please enter a number you want to divide it with"))
    result = x/y
except Exception as e:
    print("There is an error nigga")
else:
    print(result)
finally:
    print("Try all you like i will always execute")