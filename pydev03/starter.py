def fibR(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return ( fibR(n-1) + fibR(n-2) );

def fibRLessThanNImpl(n, a, b, i):
    if a < n:
        print(' fib({}) := {}'.format(i, a), end = '\n');
        fibRLessThanNImpl(n, b, a + b, i + 1);

def fibRLessThanN(n):
    fibRLessThanNImpl(n, 0, 1, 0);

def fibLessThanN(n):
    a, b = 0, 1;
    i = a;
    while a < n:
        print(' fib({}) := {}'.format( i, a ), end = '\n');
        a, b = b, a + b;
        i += 1;

def printLine(i):
    print(100 *'-', end = ' {}\n'.format(i));

# number = int(input('Print a number: \n'));

# print(fibR(number));

a = 0;

max = 2000;

printLine(1);
while fibR(a) < max:
    print(' fib({}) := {}'.format( a, fibR(a) ), end = '\n');
    a += 1;

printLine(2);
fibRLessThanN(max);
printLine(3);
fibLessThanN(max);
