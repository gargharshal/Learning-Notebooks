# Import NumPy as its abbreviation 'np'
import numpy as np


# Create an array of normally distributed random numbers
np.random.randn(3, 5)


# Create a 1-dimensional NumPy array using np.array()
x = np.random.randn(3, 1)

# Create a 2-dimensional NumPy array using np.array()
y = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 3-dimensional Numpy array using np.array()
z = np.random.rand(1, 2, 4)
x, y, z


# Attributes of 3-dimensional array
z.shape, type(z), z.dtype, z.size


# Import pandas and create a DataFrame out of one
# of the arrays you've created
import pandas as pd

df = pd.DataFrame(y)
df


# Create an array of shape (10, 2) with only ones
np.ones((10, 2))


# Create an array within a range of 0 and 100 with step 3
np.arange(0, 100, 3)


# Create an array with 10 evenly spaced numbers between 1 and 100
np.linspace(1, 100, 10,
            endpoint=True) # by default True


# Create a random array with numbers between 0 and 10 of size (7, 2)
x = np.random.randint(0, 10, size = (7, 2))
x.shape, x


# Create a random array of floats between 0 & 1 of shape (3, 5)
np.random.rand(3, 5)


# Set the random seed to 42
np.random.seed(42)

# Create a random array of numbers between 0 & 10 of size (4, 6)
np.random.randint(0, 10, size = (4, 6))


# Create an array of random numbers between 1 & 10 of size (3, 7)
# and save it to a variable
x = np.random.randint(0, 10, size = (3, 7))
print(x)
# Find the unique numbers in the array you just created
np.unique(x)


# Find the 0'th index of the latest array you created
x[0]


# Get the first 2 rows of latest array you created
x[0:2]


# Get the first 2 values of the first 2 rows of the latest array
x[:2, :2]


# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables
x = np.random.randint(0, 10, size = (3, 5))
y = np.ones((3, 5))

x, y


# Add the two arrays together
x + y


# Create another array of ones of shape (5, 3)
z = np.ones((5, 3))


# Try add the array of ones and the other most recent array together
# x + z
# this won't work, why?
# ValueError: operands could not be broadcast together with shapes (3,5) (5,3) 


# Create another array of ones of shape (3, 5)
a = np.ones((3, 5))
a


# Subtract the new array of ones from the other most recent array
x - a


# Multiply the ones array with the latest array
a*x


# Take the latest array to the power of 2 using '**'
x**2 


get_ipython().run_cell_magic("time", "", """# Do the same thing with np.square()
np.power(x, 100) # np.square(x)""")


# Find the mean of the latest array using np.mean()
# Find the maximum of the latest array using np.max()
# Find the minimum of the latest array using np.min()
# Find the standard deviation of the latest array
np.std(x), np.std(x, axis = 1), np.std(x, axis = 0)
# Find the variance of the latest array


# Reshape the latest array to (3, 5, 1)
np.reshape(x, (3, 5, 1))


# Transpose the latest array
x.T


# Create two arrays of random integers between 0 to 10
# one of size (3, 3) the other of size (3, 2)
a1 = np.random.randint(0, 10, size = (3, 3))
a2 = np.random.randint(0, 10, size = (3, 2))
a1, a2


# Perform a dot product on the two newest arrays you created
a1.dot(a2) # a2.dot(a1), this will not work 


np.dot(a1, a2) # np.dot(a2, a1), this will not work


# Create two arrays of random integers between 0 to 10
# both of size (4, 3)
b1 = np.random.randint(0, 10, size = (4, 3))
b2 = np.random.randint(0, 10, size = (4, 3))
b1, b2


# Perform a dot product on the two newest arrays you created
# np.dot(b1, b2)
# this won't work, why?
# ValueError: shapes (4,3) and (4,3) not aligned: 3 (dim 1) get_ipython().getoutput("= 4 (dim 0)")


# Take the latest two arrays, perform a transpose on one of them and then perform 
# a dot product on them both
np.dot(b1, b2.T) # or np.dot(b2, b1.T)


# Compare the two arrays with '>='
b1 >= b2


# Find which elements of the first array are greater than 7
b1 > 7


# Sort one of the arrays you just created in ascending order
b1, np.sort(b1), np.sort(b1, axis = 0)



-np.sort(-b1) # reverse sort


# Sort the indexes of one of the arrays you just created
np.argsort(b1)


# Find the index with the maximum value in one of the arrays you've created
# Find the index with the minimum value in one of the arrays you've created
b1, np.argmax(b1), np.argmin(b1)


# Find the indexes with the maximum values down the verticial axis
# of one of the arrays you created
np.argmax(b1, axis = 1), np.argmin(b1, axis = 1)


# Find the indexes with the minimum values across the horizontal axis
# of one of the arrays you created
np.argmax(b1, axis = 0), np.argmin(b1, axis = 0)


b1.sum(axis = 0)
