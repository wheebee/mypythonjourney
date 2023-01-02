name = "SeoWhi"
print (isinstance(name, str))

age = float(2)
print(isinstance(age, float))

age = int(2.9)
print(isinstance(age, int))

age = int ("30")
print(isinstance(age, int))

name += " is my name"
print(name)

print("""Seowhi is

30

years old
""")

print("seowhi".upper())
print("seowhi is cool".title())
print(len(name))

done = False
if done:
    print("yes")
else:
    print ("no")

    
names = ("seowhi", "cool")

print(names[0])
print(names.index("seowhi"))
newTuple = names + ("john", "quincy")
print(newTuple)

dog = { "name": "Roger", "age": 8 }

print(dog["name"])