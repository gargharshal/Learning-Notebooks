# Import the pyplot module from matplotlib as plt and make sure 
# plots appear in the notebook using 'get_ipython().run_line_magic("matplotlib", " inline'")
get_ipython().run_line_magic("matplotlib", " inline")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create a simple plot using plt.plot()
plt.plot()


# Plot a single Python list
list1 = [3, 4, 1]
plt.plot(list1)


# Create two lists, one called X, one called y, each with 5 numbers in them
X = [1, 3, 4, 5, 2]
y = [9, 2, 4, 7, 9]



# Plot X & y (the lists you've created)
# 2 graphs on same axis
plt.plot(X)
plt.plot(y)


# 1 graph on different axis
plt.plot(X, y)


# Create a plot using plt.subplots() and then add X & y on the axes
fig, ax  = plt.subplots(nrows = 2, ncols = 1)
ax[0].plot(X)
ax[1].plot(y)



# Import and get matplotlib ready


# Prepare data (create two lists of 5 numbers, X & y)


# Setup figure and axes using plt.subplots()
fig, ax = plt.subplots()

# Add data (X, y) to axes
ax.plot(X, y)

# Customize plot by adding a title, xlabel and ylabel
ax.set(xlabel = 'X',
      ylabel = 'y',
      title = 'sample plot')


# Save the plot to file using fig.savefig()
fig.savefig("sample_fig1.png")


# Create an array of 100 evenly spaced numbers between 0 and 100 using NumPy and save it to variable X
X = np.linspace(0, 10, 100)


# Create a plot using plt.subplots() and plot X versus X^2 (X squared)
fig, ax = plt.subplots()
ax.plot(X, np.square(X))


# Create a scatter plot of X versus the exponential of X (np.exp(X))
plt.scatter(X, np.exp(X))


# Create a scatter plot of X versus np.sin(X)
plt.scatter(X, np.sin(X))


# Create a Python dictionary of 3 of your favourite foods with 
# The keys of the dictionary should be the food name and the values their price
food = {
    'food1' : 10,
    'food2' : 20,
    'food3' : 30
}
# Create a bar graph where the x-axis is the keys of the dictionary
# and the y-axis is the values of the dictionary


# Add a title, xlabel and ylabel to the plot
plt.bar(food.keys(), food.values())
plt.xlabel("food")
plt.ylabel("price")
plt.title("Food price list")


# Make the same plot as above, except this time make the bars go horizontal
plt.barh(list(food.keys()), # it works a little differently in horizontal bar graph
         food.values())


# Create a random NumPy array of 1000 normally distributed numbers using NumPy and save it to X
X = np.random.randn(10000, 1)

# Create a histogram plot of X
plt.hist(X, bins = 100);


# Create a NumPy array of 1000 random numbers and save it to X
X = np.random.rand(10000, 1)

# Create a histogram plot of X
plt.hist(X, bins = 100);


# Create an empty subplot with 2 rows and 2 columns (4 subplots total)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2)



# Create the same plot as above with 2 rows and 2 columns and figsize of (10, 5)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2)

ax1.plot(X, X/2)

# Plot a scatter plot of 10 random numbers on each axis on the top right subplot
ax2.scatter(np.random.random(10), np.random.random(10))

# Plot a bar graph of the favourite food keys and values on the bottom left subplot
ax3.bar(food.keys(), food.values())

# Plot a histogram of 1000 random normally distributed numbers on the bottom right subplot
ax4.hist(np.random.randn(1000));


# Import the '../data/car-sales.csv' into a DataFame called car_sales and view
df = pd.read_csv('car-sales.csv')
df.head()


# Try to plot the 'Price' column using the plot() function
# plt['Price'].plot(df)


# Remove the symbols, the final two numbers from the 'Price' column and convert it to numbers
df['Price'] = df['Price'].str.replace('[/./,/$]', '')
df['Price'] = df['Price'].str[:-2].astype(int)
df['Price']


import datetime as dt
# Add a column called 'Total Sales' to car_sales which cumulatively adds the 'Price' column
df['Total Sales'] = df['Price'].cumsum()

# Add a column called 'Sale Date' which lists a series of successive dates starting from today (your today)
df['Date'] = pd.date_range(start=dt.date.today(), periods=len(df), freq='D')

# View the car_sales DataFrame
df


# Use the plot() function to plot the 'Sale Date' column versus the 'Total Sales' column
# plt.plot(df['Date'], df['Total Sales'])
df.plot('Date', 'Total Sales') # produce a better result visually 


# Create a scatter plot of the 'Odometer (KM)' and 'Price' column using the plot() function
plt.scatter(df['Odometer (KM)'], df['Price'])


# Import "../data/heart-disease.csv" and save it to the variable "heart_disease"
hd = pd.read_csv('heart-disease.csv')
hd.head()


# Create a histogram of the "age" column with 50 bins
hd.hist('age', bins = 50)


# Call plot.hist() on the heart_disease DataFrame and toggle the
# "subplots" parameter to True
hd.plot(subplots = True, kind = 'hist');


# Call the same line of code from above except change the "figsize" parameter
# to be (10, 30)

hd.plot(subplots = True, 
        kind = 'hist',
        figsize = (10, 30));


# easier way
hd.hist(figsize = (10, 10));


# Replicate the above plot in whichever way you see fit

# Note: The method below is only one way of doing it, yours might be
# slightly different

# Create DataFrame with patients over 50 years old
hd50 = hd[hd['age'] > 50]

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the data
scatter = plt.scatter(hd50['age'], hd50['chol'], c = hd50['target'])

# Customize the plot
plt.xlabel('Age')
plt.ylabel('Cholestrol')
plt.title('Heart Disease and Cholesterol Levels')
plt.legend(*scatter.legend_elements(), title = 'Target')

# Add a meanline
plt.axhline(hd['chol'].mean(),
           linestyle = '--')


# Check what styles are available under plt
plt.style.available


# Change the style to use "seaborn-whitegrid"
plt.style.use("seaborn-whitegrid")


# Reproduce the same figure as above with the "seaborn-whitegrid" style

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the data
scatter = plt.scatter(hd50['age'], hd50['chol'], c = hd50['target'])

# Customize the plot
plt.xlabel('Age')
plt.ylabel('Cholestrol')
plt.title('Heart Disease and Cholesterol Levels')
plt.legend(*scatter.legend_elements(), title = 'Target')

# Add a meanline
plt.axhline(hd['chol'].mean(),
           linestyle = '--');


# Replot the same figure as above except change the "cmap" parameter
# of scatter() to "winter"
# Also change the "color" parameter of axhline() to "red"

hd50 = hd[hd['age'] > 50]

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the data
scatter = plt.scatter(hd50['age'], hd50['chol'], c = hd50['target'], cmap = 'winter')

# Customize the plot
plt.xlabel('Age')
plt.ylabel('Cholestrol')
plt.title('Heart Disease and Cholesterol Levels')
plt.legend(*scatter.legend_elements(), title = 'Target')

# Add a meanline
plt.axhline(hd['chol'].mean(),
           linestyle = '--',
           color = 'red');


# Save the current figure using savefig(), the file name can be anything you want
plt.savefig('complete_fig.png')


# Reset the figure by calling plt.subplots()
plt.subplots()
