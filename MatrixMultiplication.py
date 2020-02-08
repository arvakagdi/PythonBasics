'''
Matrix multiplication using Strassen algorithm

Inputs: 2 matrices 
Ouput: Resultant matrix using numpy
'''

import numpy as np       #imports numpy library
import time              #imports time library

#Generating random numbers in both matrix using numpy random.rand function
MatrixOne = np.random.rand (1000,620)        
MatrixTwo = np.random.rand (620,500)

tic = time.time()        #calculates time before execution of multiplication
ResultMatrix = np.dot(MatrixOne,MatrixTwo)
toc = time.time()        #calculates time after multiplication


print("Matrix 1: " , MatrixOne)
print("Matrix 2: " , MatrixTwo)
print("Resultant Matrix: " , ResultMatrix)
print("Time taken: ", (toc-tic) * 1000 , "ms")
