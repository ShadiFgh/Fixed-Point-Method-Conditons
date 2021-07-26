import numpy as np

def find_fixed_point(f, x, itr):
    while itr:
         x = f(x)
         print(x)
         itr = itr - 1
    return x

print('Enter coefficients whit space after each coefficient exept the last. \n Eexample :"1 2 3 4"\n')
coef = list(map(float, input('Please enter the Coefficients:').split(' ')))
poly = np.poly1d(coef)
print(poly)
poly2 = np.polyder(poly)
print('Please enter the beginnig point of the domain:')
a = float(input())
print('Please enter the ending point of the domain:')
b = float(input())
roots = np.roots(poly2)
R =[]
for i in roots:
    if np.isreal(i) == 1 and a <= i <= b:
        R.append(poly(i))
R.append(poly(a))
R.append(poly(b))

flag1 = 0
if max(R) <= b and a <= min(R) :
    print('The first condition is accepted')
    flag1 = 1
else: print('The first condition is not accepted')


poly3 = np.polyder(poly2)
roots2 = np.roots(poly3)
R2 =[]

for i in roots2:
    if np.isreal(i) == 1 and a <= i <= b:
        R2.append(abs(poly2(i)))
R2.append(abs(poly2(a)))
R2.append(abs(poly2(b)))

flag2 = 0
if 0 < max(R2) < 1 :
    print('The second condition is accepted')
    flag2 = 1
else: print('The second condition is not accepted')