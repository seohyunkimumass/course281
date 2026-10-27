"""arrays_slicing.py 9/29/26 SeoHyun Kim
array slicing.
"""

import numpy as np

rr = int(input('rows? '))   # asking row
cc = int(input('cols? '))   # asking column
aa = np.zeros((rr,cc),int)  # creating array with zeros
tc = np.array([])           # creating empty array for third column

for r in range(rr):         # Replacing zeros with numbers
    for c in range(cc):
        aa[r,c] = r*cc + (c+1)
    
print('Array:\n',aa)    
print('Third column: ',aa[:rr,2])
print('Fifth row: ',aa[4])
print('Upper left:\n',aa[:3,:3])
print('Upper right:\n',aa[:3,-3:])
print('Transpose:\n',aa.T)

np.savetxt('foo.txt',aa,newline='\r\n',fmt='%10.6f')
np.savetxt('data.csv',aa,newline='\r\n',fmt='%3d', header='data2  Oct 01 2026\r\nx1,x2,x3,x4,x5',comments='')


