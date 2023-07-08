"""
Create a 3x3 array that contains a diagonal of nines
"""

import numpy as np
x = np.zeros((3,3),dtype=int)
for i in range(3):
    x[i][i]=9
print(x)
