
list_var = list(map(lambda x: x, range(10)))
tuple_var = tuple(map(lambda x: x, range(len(list_var))))
list_names = ['Thomas', 'Jeremy', 'Louise', 'Kevin', 'Justin']
dict_var = dict(map(lambda x: (list_names[x], [x,]), range(len(list_names))))
tuple_var1 = (('Mike', 1, 300), ('John', 7, 900))
dict_var1 = dict(map(lambda x: (x[0], list(x[1:])), tuple_var1))
list_var1 = [1, 2, 2, 6, 9, 6]
set_var = set(list_var1);

print(list_var)
print(tuple_var)
print(list_names)
dict_var['Jeremy'].append(12)
print(dict_var)
print(tuple_var1)
print(dict_var1)
print(list_var1)
print(set_var)
