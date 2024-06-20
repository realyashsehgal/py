print("So here i am creating a basic si string like Mugiwara no luffy")
name = "Mugiwara No Luffy"
print(len(name))
print(name[1])
#continue from string slicing
#hehe this new thing is string slicinig it works like this 
#string name[start:stop:step]
#lemme show you
first_name = name[0:8]
middle_name = name[9:11]
last_name = name[12:len(name)]
print(first_name)
print(middle_name)
print(last_name)
#Now i will show how you can skip some chaaracters from this string like this
divide = name[0:len(name):2]
print(divide)
#thats it huh neh i will show you how to print in reverse 
reverse = name[::-1]
print(reverse)


#string slicing the url of any website with .com ending
website = "https//:google.com"
website2 = "https//:wikipedia.com"
slice = slice(8,-4)
print(website[slice])
print(website2[slice])