# Import NumPy as its abbreviation 'np'
import numpy as np


# Create a 1-dimensional NumPy array using np.array()
x = np.random.randn(3, 1)

# Create a 2-dimensional NumPy array using np.array()
y = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 3-dimensional Numpy array using np.array()
z = np.random.rand(1, 2, 4)
x, y, z


# Attributes of 1-dimensional array (shape, 
# number of dimensions, data type, size and type)



# Attributes of 2-dimensional array



# Attributes of 3-dimensional array
z.shape, type(z), z.dtype, z.size


# Import pandas and create a DataFrame out of one
# of the arrays you've created
import pandas as pd

df = pd.DataFrame(y)
df


# Create an array of shape (10, 2) with only ones
np.ones((10, 2))


# Create an array of shape (7, 2, 3) of only zeros



# Create an array within a range of 0 and 100 with step 3



# Create a random array with numbers between 0 and 10 of size (7, 2)



# Create a random array of floats between 0 & 1 of shape (3, 5)



# Set the random seed to 42


# Create a random array of numbers between 0 & 10 of size (4, 6)



# Create an array of random numbers between 1 & 10 of size (3, 7)
# and save it to a variable


# Find the unique numbers in the array you just created



# Find the 0'th index of the latest array you created



# Get the first 2 rows of latest array you created



# Get the first 2 rows of latest array you created



# Get the first 2 values of the first 2 rows of the latest array



# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables



# Add the two arrays together



# Create another array of ones of shape (5, 3)



# Try add the array of ones and the other most recent array together



# Create another array of ones of shape (3, 5)



# Subtract the new array of ones from the other most recent array



# Multiply the ones array with the latest array



# Take the latest array to the power of 2 using '**'



# Do the same thing with np.square()



# Find the mean of the latest array using np.mean()



# Find the maximum of the latest array using np.max()



# Find the minimum of the latest array using np.min()



# Find the standard deviation of the latest array



# Find the variance of the latest array



# Reshape the latest array to (3, 5, 1)



# Transpose the latest array



# Create two arrays of random integers between 0 to 10
# one of size (3, 3) the other of size (3, 2)



# Perform a dot product on the two newest arrays you created



# Create two arrays of random integers between 0 to 10
# both of size (4, 3)



# Perform a dot product on the two newest arrays you created



# Take the latest two arrays, perform a transpose on one of them and then perform 
# a dot product on them both



# Create two arrays of random integers between 0 & 10 of the same shape
# and save them to variables



# Compare the two arrays with '>'



# Compare the two arrays with '>='



# Find which elements of the first array are greater than 7



# Which parts of each array are equal? (try using '==')



# Sort one of the arrays you just created in ascending order



# Sort the indexes of one of the arrays you just created



# Find the index with the maximum value in one of the arrays you've created



# Find the index with the minimum value in one of the arrays you've created



# Find the indexes with the maximum values down the verticial axis
# of one of the arrays you created



# Find the indexes with the minimum values across the horizontal axis
# of one of the arrays you created



# Create an array of normally distributed random numbers



# Create an array with 10 evenly spaced numbers between 1 and 100

