import numpy as np
import math as math
x1 = float(input('Input value of x1: '))
x2 = float(input('Input value of x2: '))
x3 = float(input('Input value of x3: '))
y1 = float(input('Input value of y1: '))
y2 = float(input('Input value of y2: '))
y3 = float(input('Input value of y3: '))

x1a = x1**2 + y1**2
x2a = x2**2 + y2**2
x3a = x3**2 + y3**2
    
C = np.array([(x1, y1, 1), (x2, y2, 1), (x3, y3, 1)])
D = -np.array([(x1a, y1, 1), (x2a, y2, 1), (x3a, y3, 1)])
E = np.array([(x1a, x1, 1), (x2a, x2, 1), (x3a, x3, 1)])
F = -np.array([(x1a, x1, y1), (x2a, x2, y2), (x3a, x3, y3)])
    
h = -((round(np.linalg.det(D))) / (2*round(np.linalg.det(C))))
k = -((round(np.linalg.det(E))) / (2*round(np.linalg.det(C))))
    
D_val = (round(np.linalg.det(D)))/ (round(np.linalg.det(C)))
E_val = (round(np.linalg.det(E))) / (round(np.linalg.det(C)))
F_val = (round(np.linalg.det(F))) / (round(np.linalg.det(C)))
    
r = round(math.sqrt((h - x1)**2 + (k - y1)**2))
    
print('Center: (',h,',',k,')')
print('Radius: r = ',r,' units')
print('Vector: [',D_val,',',E_val,',',F_val,']')