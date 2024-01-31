
dict = { (1, 2): 4, (3, 5): 2 }
arr = [];

for key, value in dict.items():
    # singleton = value,
    # arr.append(key + singleton)
    arr.append(key + (value,))

print(arr)
