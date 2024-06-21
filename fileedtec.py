import os
# path = "C:\\Users\\yashs\\OneDrive\\Desktop\\coding\\py\\.vscode"
# if os.path.exists(path):
#     print("damn tha file exist huh")
# if os.path.isdir(path):
#     print("brotha its a dir damnnnn")
# else:
#     print("dude check file name might be wrong")





# try:    
#     with open('myfile.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("brotha check file name")


text = "This is some random bull shit i just came up with\n because \n i want to write in the file heheheheh"
with open('myfile.txt','w') as file:
    file.write(text)
with open('myfile.txt', 'r') as file:
    print(file.read())
print("so you can just append it easily using mode a")