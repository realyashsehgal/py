import random # type: ignore
n =random.randint(1,10)
print(n) # type: ignore
mylist = ['rock','paper','scisor']
z = random.choice(mylist)
print(z)
deck = [1,2,3,4,5,6,7,8,9,'jack','queen','king']
random.shuffle(deck)
print(deck)