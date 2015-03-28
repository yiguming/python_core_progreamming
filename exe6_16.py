#!/usr/bin/env python
#sudo apt-get install python-numpy
from numpy import matrix 
M = matrix('1,2,3;2,3,4;3,4,5')
N = matrix('1,2,3;2,3,4;3,4,5')
print M+N
print M*N
