import random as rd
#help(rd)

print(rd.randint(1, 10))


# some methods in random module

# rd.random() #random float between 0 and 1
# rd.randint(1, 10) #random integer between 1 and 10
# rd.choice([1, 2, 3, 4, 5]) #random choice from a list
# rd.choices([1, 2, 3, 4, 5], k=2) #random choice from a list with replacement, k is the number of choices
# rd.shuffle([1, 2, 3, 4, 5]) #shuffles the list in place
# rd.sample([1, 2, 3, 4, 5], k=2) #random sample from a list without replacement, k is the number of samples
# rd.uniform(1, 10) #random float between 1 and 10
 
 
