#these follows hashmap heh
#like
capital = {'USA':'Washington DC',
           'India' : 'New Delhi',
           'Russia' : 'Moscow'}
print("Okay so i have made a hashmap with some key values lets see")
print(capital.get('Russia'))
print("Well thats not it i can print even the key values")
print(capital.keys())
print("hmmmm...... so lemme show the values in those keys")
print(capital.values())
print("haah see now i will print them all together")
print(capital.items())
print("Okay okay so i am updating the dictionay with a new country and its capital which is germany")
capital.update({'germany':'berlin'})
print(capital.get('germany'))