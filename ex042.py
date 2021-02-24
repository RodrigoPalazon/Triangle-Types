print('-=' * 20)
print('Triangle Analyzer')
print('-=' * 20)
r1 = float(input('Type the first side of a triangle: '))
r2 = float(input('Type the second side of a triangle: '))
r3 = float(input('Type the third side of a triangle: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('It`s possible to make a triangle')
    if r1 == r2 and r2 == r3: # r1==r2==r3
        print('This is an EQUILATERAL TRIANGLE (3 equal sides).')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('This is an ISOSCELES TRIANGLE (2 equal sides).')
    else:
        print('This is an ESCALENO TRIANGLE (all different sides).')
else:
    print('It`s NOT possible to make a triangle with these lines')
