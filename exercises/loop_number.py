squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)

print (squares)
print min(squares)
print max(squares)
print sum(squares)

#the following will look at the list comprehesion. Used primarily to make shorter code

squares = [value**2 for value in range(1,11)]

print (squares)

# Exercise 4-3

twenty = []

for value in range(1,21):
    twenty.append(value)

print (twenty)

# Exercise 4-4 

million = []

for value in range(1,1000001):
    million.append(value)
    print (value)


# Exercise 4-5

print min(million)
print max(million)
print sum(million)

# Exercise 4-6
for value in range(1,21,2):
    print (value)

# Exercise 4-7
for value in range (3,31,3):
    print value

# Exercise 4-8
cubes = [value**3 for value in range(1,11)]
print (cubes)