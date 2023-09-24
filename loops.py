# loops in python

# for loop

for i in range(1, 10):
    print(i)


# while loop

i = 1
while i < 10:
    print(i)
    i += 1

# break statement

i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1


# continue statement

i = 1
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


# pass statement

i = 1
while i < 10:
    i += 1
    if i == 5:
        pass
    print(i)


# else statement

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("i is greater than 10")


# nested loops

for i in range(1, 10):
    for j in range(1, 10):
        print(i, j)


# loop with else

for i in range(1, 10):
    print(i)
else:
    print("i is greater than 10")


# loop with else and break

for i in range(1, 10):
    print(i)
    if i == 5:
        break
else:
    print("i is greater than 10")


# loop with else and continue

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
else:
    print("i is greater than 10")


# loop with else and pass

for i in range(1, 10):
    print(i)
    if i == 5:
        pass  # the difference b/w continue and pass is that continue will skip the current iteration and pass will do nothing
else:
    print("i is greater than 10")
