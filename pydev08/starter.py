
dict_var = { 'Bob': ( 1, True ), 'Mike' : ( 23, False) }
tuples_in_tuple = ()
lists_in_tuple = ()
dicts_in_tuple = ()
list_var = []
tuple_var = ()

tuples_in_tuple = tuple( x for x in [ (key,) + value for key, value in dict_var.items() ] )
lists_in_tuple = tuple( list(x) for x in [ (key,) + value for key, value in dict_var.items() ] )
dicts_in_tuple = tuple( { key: value } for key, value in dict_var.items() )

for key, value in dict_var.items():
    singleton = key,
    list_var.extend( list( singleton + value ) )

tuple_var = tuple(list_var)

print('dict_var:', dict_var)
print('tuples_in_tuple:', tuples_in_tuple)
print('lists_in_tuple:', lists_in_tuple)
print('dicts_in_tuple:', dicts_in_tuple)
print('list_var:', list_var)
print('tuple_var:', tuple_var)
