
var1 = 2;
var2 = 3;

isEqual = var1 == var2;

match isEqual:
    case True:
        print('They are the same number');
    case False:
        print('They are not the same number!');
