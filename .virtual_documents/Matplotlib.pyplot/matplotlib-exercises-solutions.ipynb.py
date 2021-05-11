# Import the pyplot module from matplotlib as plt and make sure 
# plots appear in the notebook using 'get_ipython().run_line_magic("matplotlib", " inline'")
get_ipython().run_line_magic("matplotlib", " inline")
import matplotlib.pyplot as plt 


# Create a simple plot using plt.plot()
plt.plot()


# Plot a single Python list
plt.plot([2, 6, 8, 17])


# Create two lists, one called X, one called y, each with 5 numbers in them
X = [22, 88, 98, 103, 45]
y = [7, 8, 9, 10, 11]


# Plot X & y (the lists you've created)
plt.plot(X, y)


# Create a plot using plt.subplots()
fig, ax = plt.subplots()


# Create a plot using plt.subplots() and then add X & y on the axes
fig, ax = plt.subplots()
ax.plot(X, y)


# Import and get matplotlib ready
get_ipython().run_line_magic("matplotlib", " inline")
import matplotlib.pyplot as plt

# Prepare data (create two lists of 5 numbers, X & y)
X = [34, 77, 21, 54, 9]
y = [9, 45, 89, 66, 4]

# Setup figure and axes using plt.subplots()
fig, ax = plt.subplots()

# Add data (X, y) to axes
ax.plot(X, y)

# Customize plot by adding a title, xlabel and ylabel
ax.set(title="Sample simple plot",
       xlabel="x-axis",
       ylabel="y-axis")

# Save the plot to file using fig.savefig()
fig.savefig("../images/simple-plot.png")


# Import NumPy as np
import numpy as np


# Create an array of 100 evenly spaced numbers between 0 and 100 using NumPy and save it to variable X
X = np.linspace(0, 10, 100)


# Create a plot using plt.subplots() and plot X versus X^2 (X squared)
fig, ax = plt.subplots()
ax.plot(X, X**2)


# Create a scatter plot of X versus the exponential of X (np.exp(X))
fig, ax = plt.subplots()
ax.scatter(X, np.exp(X))


# Create a scatter plot of X versus np.sin(X)
fig, ax = plt.subplots()
ax.scatter(X, np.sin(X))


# Create a Python dictionary of 3 of your favourite foods with 
# The keys of the dictionary should be the food name and the values their price
favourite_food_prices = {"Almond butter": 10,
                         "Blueberries": 5,
                         "Eggs": 6}


# Create a bar graph where the x-axis is the keys of the dictionary
# and the y-axis is the values of the dictionary
fig, ax = plt.subplots()
ax.bar(favourite_food_prices.keys(), favourite_food_prices.values())

# Add a title, xlabel and ylabel to the plot
ax.set(title="Daniel's favourite foods",
       ylabel="Food",
       xlabel="Price ($)")


# Make the same plot as above, except this time make the bars go horizontal
fig, ax = plt.subplots()
ax.barh(list(favourite_food_prices.keys()),
        list(favourite_food_prices.values()))
ax.set(title="Daniel's favourite foods",
       xlabel="Price ($)",
       ylabel="Food")


# Create a random NumPy array of 1000 normally distributed numbers using NumPy and save it to X
X = np.random.randn(1000)

# Create a histogram plot of X
fig, ax = plt.subplots()
ax.hist(X)


# Create a NumPy array of 1000 random numbers and save it to X
X = np.random.random(1000)

# Create a histogram plot of X
fig, ax = plt.subplots()
ax.hist(X)


# Create an empty subplot with 2 rows and 2 columns (4 subplots total)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2,
                                             ncols=2)


# Create the same plot as above with 2 rows and 2 columns and figsize of (10, 5)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2,
                                             ncols=2,
                                             figsize=(10, 5))

# Plot X versus X/2 on the top left axes
ax1.plot(X, X/2)

# Plot a scatter plot of 10 random numbers on each axis on the top right subplot
ax2.scatter(np.random.random(10), np.random.random(10))

# Plot a bar graph of the favourite food keys and values on the bottom left subplot
ax3.bar(favourite_food_prices.keys(), favourite_food_prices.values())

# Plot a histogram of 1000 random normally distributed numbers on the bottom right subplot
ax4.hist(np.random.randn(1000));


# Import pandas as pd
import pandas as pd


# Import the '../data/car-sales.csv' into a DataFame called car_sales and view
car_sales = pd.read_csv("../data/car-sales.csv")
car_sales


# Try to plot the 'Price' column using the plot() function
car_sales["Price"].plot()


# Remove the symbols, the final two numbers from the 'Price' column and convert it to numbers
car_sales["Price"] = car_sales["Price"].str.replace("[\$\,\.]", "")
car_sales["Price"] = car_sales["Price"].str[:-2]


# Add a column called 'Total Sales' to car_sales which cumulatively adds the 'Price' column
car_sales["Total Sales"] = car_sales["Price"].astype(int).cumsum()

# Add a column called 'Sale Date' which lists a series of successive dates starting from today (your today)
car_sales["Sale Date"] = pd.date_range("13/1/2020", periods=len(car_sales))

# View the car_sales DataFrame
car_sales


# Use the plot() function to plot the 'Sale Date' column versus the 'Total Sales' column
car_sales.plot(x="Sale Date", y="Total Sales")


# Convert the 'Price' column to the integers
car_sales["Price"] = car_sales["Price"].astype(int)

# Create a scatter plot of the 'Odometer (KM)' and 'Price' column using the plot() function
car_sales.plot(x="Odometer (KM)", y="Price", kind="scatter")


# Create a NumPy array of random numbers of size (10, 4) and save it to X
X = np.random.rand(10, 4)

# Turn the NumPy array X into a DataFrame with columns called ['a', 'b', 'c', 'd']
df = pd.DataFrame(X, columns=["a", "b", "c", "d"])

# Create a bar graph of the DataFrame
df.plot(kind="bar")


# Create a bar graph of the 'Make' and 'Odometer (KM)' columns in the car_sales DataFrame
car_sales.plot(x="Make", y="Odometer (KM)", kind="bar")


# Create a histogram of the 'Odometer (KM)' column
car_sales["Odometer (KM)"].plot(kind="hist")


# Create a histogram of the 'Price' column with 20 bins
car_sales["Price"].plot.hist(bins=20)


# Import "../data/heart-disease.csv" and save it to the variable "heart_disease"
heart_disease = pd.read_csv("../data/heart-disease.csv")


# View the first 10 rows of the heart_disease DataFrame
heart_disease.head(10)


# Create a histogram of the "age" column with 50 bins
heart_disease["age"].plot.hist(bins=50);


# Call plot.hist() on the heart_disease DataFrame and toggle the
# "subplots" parameter to True
heart_disease.plot.hist(subplots=True);


# Call the same line of code from above except change the "figsize" parameter
# to be (10, 30)
heart_disease.plot.hist(figsize=(10, 30), subplots=True);


# Replicate the above plot in whichever way you see fit

# Note: The method below is only one way of doing it, yours might be
# slightly different

# Create DataFrame with patients over 50 years old
over_50 = heart_disease[heart_disease["age"] > 50]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
scatter = ax.scatter(over_50["age"], 
                     over_50["chol"], 
                     c=over_50["target"])

# Customize the plot
ax.set(title="Heart Disease and Cholesterol Levels",
       xlabel="Age",
       ylabel="Cholesterol");
ax.legend(*scatter.legend_elements(), title="Target")

# Add a meanline
ax.axhline(over_50["chol"].mean(),
           linestyle="--");


# Check what styles are available under plt
plt.style.available


# Change the style to use "seaborn-whitegrid"
plt.style.use("seaborn-whitegrid")


# Reproduce the same figure as above with the "seaborn-whitegrid" style

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
scatter = ax.scatter(over_50["age"], 
                     over_50["chol"], 
                     c=over_50["target"])

# Customize the plot
ax.set(title="Heart Disease and Cholesterol Levels",
       xlabel="Age",
       ylabel="Cholesterol");
ax.legend(*scatter.legend_elements(), title="Target")

# Add a meanline
ax.axhline(over_50["chol"].mean(),
           linestyle="--");


# Replot the same figure as above except change the "cmap" parameter
# of scatter() to "winter"
# Also change the "color" parameter of axhline() to "red"

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
scatter = ax.scatter(over_50["age"], 
                     over_50["chol"], 
                     c=over_50["target"],
                     cmap="winter") # changed cmap parameter

# Customize the plot
ax.set(title="Heart Disease and Cholesterol Levels",
       xlabel="Age",
       ylabel="Cholesterol");
ax.legend(*scatter.legend_elements(), title="Target")

# Add a meanline
ax.axhline(over_50["chol"].mean(),
           linestyle="--",
           color="red"); # changed color parameter


# Save the current figure using savefig(), the file name can be anything you want
fig.savefig("../images/matplotlib-heart-disease-chol-age-plot-saved.png")


# Reset the figure by calling plt.subplots()
fig, ax = plt.subplots()
