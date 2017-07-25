import random

file = open("snakeLevel.txt", "r")
name = file.read()

print(name[0][10])

for i in range(0,10):
    print(random.random())


