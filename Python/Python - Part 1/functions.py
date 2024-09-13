# Filter Function

list_1 = [1,2,3,4,5,6,7,8,9,10]

def even_bool(num):
    return num%2 == 0

results = filter(even_bool, list_1)
print(list(results))

results = filter(lambda num: num%2 == 0, list_1)
print(list(results))