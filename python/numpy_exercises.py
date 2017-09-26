# find indices of non-zero elements from [1,2,0,0,4,0]
import numpy as np
#print(np.__version__)
#np.show_config()

#create a null vector of size 10
z = np.zeros(10);
z[4]=1

#create a vector with values ranging from 10 to 49
z=np.arange(10,50)

#create a vector with values ranging till 50 (excluded) starting zero
z = np.arange(50)

#reverse a vector (first element becomes last)
z = z[::-1]

#create a  3X3 matrix with values ranging from 0 to 8
z=np.arange(9).reshape(3,3)

#find indices of non-zero elements from [1,2,0,0,4,0]
z = np.nonzero([1,2,0,0,4,0])

#create a 3X3 identity matrix
z = np.eye(3)
print(z)






