import random
import numpy as np
w=[]
y=[]
n=1
m=1
import csv
while n<21:
	print(n)
	while m<31:
		xd=random.normalvariate(19,1)
		m=m+1
		w.append(xd)
	m=1
	x=np.mean(w)
	del w[:]
	y.append(x)
	n=n+1
print(np.mean(y))
print(np.nanstd(y,axis=None,dtype=None,out=None,ddof=0))
print(np.nanstd(y,axis=None,dtype=None,out=None,ddof=1))
