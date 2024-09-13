# Boolean
isLoggedIn = False # Can also use 0
isLoggedIn = True # Can also use 1

# Tuple: Lists that are immutable 
myTuple = ("apple", "banana", "cherry")
myList = [1,2,3]

print(myTuple[2])
print(myList[2])
# myTuple[2] = "Appricot" # Can not chhange values in tuple
print(myTuple[2])

# Set: Combination of unique values
mySet = {"apple", "banana", "cherry", "apple"}
print(mySet) 
test = [1,1,1,2,2,2,3,3,3]
set_2 = set(test)
print(set_2)