  
dict_var = { 'John': 300, 'James': 500, 'Mike': 120 }
dict_var1 = dict( map( lambda key: ( key, ( dict_var[key] * 0.1) ), dict_var ) )
# item[0] = key, item[1] = value
# int() convert number to integer
dict_var2 = dict( map( lambda item: ( item[0], int( item[1] * 0.1) ), dict_var.items() ) )

print(dict_var)
print(dict_var1)
print(dict_var2)
