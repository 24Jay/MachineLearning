import numpy as np

x = np.matrix([[1,1.0/7.0,1.0/3.0],[7,1,5],[3,0.2,1]])
e,v = np.linalg.eig(x)

print("X的特征值:",e)
print("X的特征向量:",v)