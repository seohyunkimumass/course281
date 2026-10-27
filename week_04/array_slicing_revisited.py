"""arrays_slicing.py 9/29/26 SeoHyun Kim
array slicing revisted.
"""

import numpy as np

a = int(input('elements? '))   # asking row \
r = int(input('rows? '))
c = int(input('columns? ')) 
aa = np.arange(1,a+1)  # creating array with zeros
bb = aa.reshape((r,c))

print(aa)
print(bb)

