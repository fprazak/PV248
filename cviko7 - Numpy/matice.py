import re # regular expressions
import numpy as np
import numpy.linalg as li
import math


# singMatrix = np.arange(9).reshape(3,3) # Singulární matice

# print(singMatrix)

randomMatrix = np.random.randint(1,10, size=(3,3))

print(randomMatrix)

det = np.linalg.det(randomMatrix)

if (det == 0):
    inv = 0
    print("Pro singulární matici neexistuje inverze")
else:
    print("Determinant je:", det)

a = np.array([[3,1], [1,2]])
b = np.array([9,8])

print("Koeficienty jsou:",np.linalg.solve(a, b))



