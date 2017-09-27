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

#create a 3X3X3 array with random values
z = np.random.random((3,3,3))

#create a 10X10 array with random values and find the minimum and maximum values
z = np.random.random((10,10))
zmin, zmax = z.min(), z.max()
#print(zmin, zmax)

#create a random vector of size 30 and find the mean value
z = np.random.random(30)
mean = z.mean()
#print(mean)

#create a 2d array with 1 on the border and 0 inside
z = np.ones((10,10))
z[1:-1, 1:-1] = 0

#what is the result of the following expression
#print(0*np.nan) #nan
#print(np.nan == np.nan) #False
#print(np.inf > np.nan) #False
#print(np.nan-np.nan) #nan
#print(0.3 == (3*0.1))  #False
#print(1==1) #True
#print(np.nan) #nan

#create a diagonal matrix of size 5 with values 1 to 5
z = np.diag(1+np.arange(5),k=0)
#print(np.arange(5))

#create a 5X5 matrix with values 1,2,3,4 just below the diagonal
z = np.diag(1+np.arange(4), k=-1)

#create a 8X8 matrix and fill it with a checkerboard pattern
z = np.zeros((8,8),dtype = int)
z[1::2, ::2] = 1
z[::2, 1::2] = 1

#consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
#print(np.unravel_index(100,(6,7,8))) #(1,5,4)

#create a checker board 8X8 matrix using the tile function
#checker_board = np.tile(np.array([[0,1],[1,0]]), (4,4))
array_pattern = np.array([[1,0],[0,1]])
size = (4,4)
checker_board= np.tile(array_pattern,size)
#print(checker_board)

#Normalize a 5X5 random matrix
z = 7 * np.random.random((5,5)) #values in the range of 0 and 7
#print(z)
zmax, zmin = z.max(), z.min()
z = (z-zmin)/(zmax-zmin)


print(z)






