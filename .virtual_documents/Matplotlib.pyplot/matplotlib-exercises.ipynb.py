# Import the pyplot module from matplotlib as plt and make sure 
# plots appear in the notebook using 'get_ipython().run_line_magic("matplotlib", " inline'")



# Create a simple plot using plt.plot()



# Plot a single Python list



# Create two lists, one called X, one called y, each with 5 numbers in them



# Plot X & y (the lists you've created)



# Create a plot using plt.subplots()



# Create a plot using plt.subplots() and then add X & y on the axes



# Import and get matplotlib ready


# Prepare data (create two lists of 5 numbers, X & y)


# Setup figure and axes using plt.subplots()


# Add data (X, y) to axes


# Customize plot by adding a title, xlabel and ylabel


# Save the plot to file using fig.savefig()



# Import NumPy as np



# Create an array of 100 evenly spaced numbers between 0 and 100 using NumPy and save it to variable X



# Create a plot using plt.subplots() and plot X versus X^2 (X squared)



# Create a scatter plot of X versus the exponential of X (np.exp(X))



# Create a scatter plot of X versus np.sin(X)



# Create a Python dictionary of 3 of your favourite foods with 
# The keys of the dictionary should be the food name and the values their price



# Create a bar graph where the x-axis is the keys of the dictionary
# and the y-axis is the values of the dictionary


# Add a title, xlabel and ylabel to the plot



# Make the same plot as above, except this time make the bars go horizontal



# Create a random NumPy array of 1000 normally distributed numbers using NumPy and save it to X


# Create a histogram plot of X



# Create a NumPy array of 1000 random numbers and save it to X


# Create a histogram plot of X



# Create an empty subplot with 2 rows and 2 columns (4 subplots total)



# Create the same plot as above with 2 rows and 2 columns and figsize of (10, 5)


# Plot X versus X/2 on the top left axes


# Plot a scatter plot of 10 random numbers on each axis on the top right subplot


# Plot a bar graph of the favourite food keys and values on the bottom left subplot


# Plot a histogram of 1000 random normally distributed numbers on the bottom right subplot



# Import pandas as pd



# Import the '../data/car-sales.csv' into a DataFame called car_sales and view



# Try to plot the 'Price' column using the plot() function



# Remove the symbols, the final two numbers from the 'Price' column and convert it to numbers



# Add a column called 'Total Sales' to car_sales which cumulatively adds the 'Price' column


# Add a column called 'Sale Date' which lists a series of successive dates starting from today (your today)

# View the car_sales DataFrame



# Use the plot() function to plot the 'Sale Date' column versus the 'Total Sales' column



# Convert the 'Price' column to the integers


# Create a scatter plot of the 'Odometer (KM)' and 'Price' column using the plot() function



# Create a NumPy array of random numbers of size (10, 4) and save it to X


# Turn the NumPy array X into a DataFrame with columns called ['a', 'b', 'c', 'd']


# Create a bar graph of the DataFrame



# Create a bar graph of the 'Make' and 'Odometer (KM)' columns in the car_sales DataFrame



# Create a histogram of the 'Odometer (KM)' column



# Create a histogram of the 'Price' column with 20 bins



# Import "../data/heart-disease.csv" and save it to the variable "heart_disease"



# View the first 10 rows of the heart_disease DataFrame



# Create a histogram of the "age" column with 50 bins



# Call plot.hist() on the heart_disease DataFrame and toggle the
# "subplots" parameter to True



# Call the same line of code from above except change the "figsize" parameter
# to be (10, 30)



# Replicate the above plot in whichever way you see fit

# Note: The method below is only one way of doing it, yours might be
# slightly different

# Create DataFrame with patients over 50 years old


# Create the plot


# Plot the data


# Customize the plot


# Add a meanline



# Check what styles are available under plt



# Change the style to use "seaborn-whitegrid"



# Reproduce the same figure as above with the "seaborn-whitegrid" style

# Create the plot


# Plot the data


# Customize the plot


# Add a meanline



# Replot the same figure as above except change the "cmap" parameter
# of scatter() to "winter"
# Also change the "color" parameter of axhline() to "red"

# Create the plot


# Plot the data


# Customize the plot


# Add a meanline



# Save the current figure using savefig(), the file name can be anything you want



# Reset the figure by calling plt.subplots()

