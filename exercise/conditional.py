# -*- coding: utf-8 -*-
x = 5
y = 6

print('x =',x,'y =', y)
print('X is less than Y:', x<y)
print('X is greater than Y:',x>y)

var_1 = 7
var_2 = 7

print('Var_1:', var_1, 'Var_2:', var_2)
print(var_1 < var_2)
print(var_1 > var_2)
print(var_1 == var_2)
print(var_1 <= var_2)
print(var_1 >= var_2)
print(var_1 != var_2)


#if statement practice 

some_condition = True

if some_condition:
    print('The variable some_condition is TRUE')
else: 
    print('The variable some_condition is False')
    
    
temp = int(input('Please enter the temperatue in Celsius. An integer between 0-40:>>>'))

if temp > 30: 
    print('It is warm outside!')
elif temp <= 30 and temp > 20:
    print('It is warm but no time to wear shorts!')
elif temp <= 20 and temp > 10: 
    print('You will probably need a coat!')
else: print('TOO COLD OUT!')