# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 2015

Modified on Fri Oct 15 2015

@author: david

"""

import LA
import numpy as np

#A=np.array([[1,2,1],[4,5,2],[4,8,3]])
A=np.array([[1,2],[4,5],[7,8]])
#A=np.array([[0,2,3],[0,5,6],[0,8,9]])
#A=np.array([[1,2,3],[3,5,6]])
print(A)
U=LA.upperTri(A)
R=LA.rref(A)
print(U)
print(R)
print(LA.det(A))
print(LA.inv(A))
b=np.array([3,6,9])
print(LA.solve(A,b))
