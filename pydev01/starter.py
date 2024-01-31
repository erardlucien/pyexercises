
numbers = [2, 5, 56, 7, 88, 79, 34, 8, 6];
NUMBERSLENGTH = len( numbers );
values = NUMBERSLENGTH * [0];
primeText = 'a prime number.';

MAX = numbers[0];

def sieb(numbers, values):
    for j in range( 2, ( MAX + 1 ) ):
        for k in range( j * j, ( MAX + 1 ), j ):
            if ( numbers[i] == k ) or ( numbers[i] == 1 or numbers[i] == 0):
                values[i] = 1;

for i in range( 1, NUMBERSLENGTH ):
    if MAX < numbers[i]:
        MAX = numbers[i];

for i in range( NUMBERSLENGTH ):
    sieb(numbers=numbers, values=values)

for i in range( NUMBERSLENGTH ):
    if(values[i] == 1):
        print( ' {} is not {}'.format(numbers[i], primeText) );
    else:
        print( ' {} is {}'.format(numbers[i], primeText) );

stars = (10 * ' * ');
print(  stars + ( 15 * '-' )  + stars );

dict0 = {};
for i in range( NUMBERSLENGTH ):
    dict0[numbers[i]] = values[i];

deletedKey  = numbers[ NUMBERSLENGTH - 1 ];

if ( deletedKey in dict0 ):
    del dict0[ deletedKey ];
    print( ' {} was deleted.'.format(deletedKey) );
else:
    print( ' {} was never part of dict0.'.format(deletedKey) );

for key in dict0:
    print( ' {} : {}'.format(key, dict0.get(key)) );
