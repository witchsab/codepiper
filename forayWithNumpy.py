import numpy as np 
import matplotlib.pyplot as plt 

x= np.arange(20,104.75, 3.6)


a = np.linspace(20,104.75, 10, endpoint=False)

print (x, a)

b = np.sin(a)
c = np.cos(a)
plt.plot (a, b)
# plt.plot (a,a)
plt.plot (a,c)

mvalues = [0,1,5,6,80]
print(mvalues)
M = np.array(mvalues)
print ('M=', M)