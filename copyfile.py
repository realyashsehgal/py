import os
# import shutil
# shutil.copy('myfile.txt','C:\\Users\\yashs\\OneDrive\\Desktop\\copy.txt') #first add src then destination
source ='myfile.txt'
destination ='C:\\Users\\yashs\\OneDrive\\Desktop\\myfile.txt'
try:
    if os.path.exists(destination):
        print("alrady there")
    else:
        os.replace(source,destination)
        print("done go find it")
except FileNotFoundError:
    print("sorry bro")