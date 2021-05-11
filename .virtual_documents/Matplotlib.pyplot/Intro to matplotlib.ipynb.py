#diff between plt.subplot() vs plt.subplots( )


get_ipython().run_line_magic("matplotlib", " inline")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.plot()


#remove the [] from above
plt.plot();


plt.plot()
plt.show()


plt.plot([1, 2, 3, 4]);


#Stateless way of ploting
x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
plt.plot(x, y)


# 1st Method
fig = plt.figure() #creates a figure
ax = fig.add_subplot() #adds some axes
plt.show()


#2nd Method
fig = plt.figure() #creates a figure
ax = fig.add_axes([1, 1, 1, 1]) #adds some axes 
ax.plot(x, y)
plt.show()


#3rd Method (recommended)
fig, ax = plt.subplots() 
ax.plot(x, [50, 100, 200, 400 ]); #add some data
type(fig) ,type(ax)


#4th method
plt.plot(x, y)


# import matplotlib and get it ready for plotting in Jupyter
get_ipython().run_line_magic("matplotlib", " inline")
import matplotlib.pyplot as plt

# 1. Prepare data
x = [1, 2, 3, 4]
y =  [11, 22, 33, 44]

# 2. Setup Plot
fig, ax = plt.subplots(figsize = (5, 5))

# 3. Plot Data
ax.plot(x, y)

# 4. Customize plot
ax.set(title = "Simple Plot",
      xlabel = "x-axis",
      ylabel = "y-axis")

# 5. save and show (you save the whole figure)
fig.savefig("sample_plot_1.jpg")


#create some daata
x = np.linspace(0, 10, 100)
x


#Plot the data and create a straight line fig 
fig, ax = plt.subplots()
ax.plot(x, x**2)


#Use the same data to draw scatter plot
fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))


#another scatter plot
fig, ax = plt.subplots()
ax.scatter(x, np.sin(x));


# Make a plot from Dictionary
#Bar Graph
nut_butter_prices = {"Almond butter": 10,
                     "Peanut butter": 8,
                     "Cashew butter": 12}
fig, ax = plt.subplots()
ax.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax.set(title = "Butter Price", ylabel = "Price", xlabel = "Butter Variety");


#Horizontal Bar Graph
#in this case we need to turn things into list
fig, ax = plt.subplots()
ax.barh(list(nut_butter_prices.keys()), list(nut_butter_prices.values()));


#Histogram
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x);


# subplot option 1
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, 
                                             ncols = 2, 
                                             figsize = (10, 5))

#plot each subplot
#or
#plot each to different axis
ax1.plot(x, x/2)
ax2.scatter(np.random.randn(20), np.random.randn(20))
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(np.random.randn(1000));


# subplot option 2
fig, ax = plt.subplots(nrows = 2,
                      ncols = 2,
                      figsize = (10, 5))

#Populate the graph
ax[0, 0].plot(x, x/2)
ax[0, 1].scatter(np.random.randn(20), np.random.randn(20))
ax[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax[1, 1].hist(np.random.randn(1000));


#Make a DataFrame


car_sales = pd.read_csv(r"C:\Users\Harshal Garg\Desktop\Z2M DS and ML\pandas\7.1 car-sales.csv.csv")
car_sales


ts = pd.Series(np.random.randn(1000),
               index = pd.date_range("1/1'/2020", periods = 1000))
ts = ts.cumsum() #cummalative sum - takes the sum of every proceding sum
ts.plot()



car_sales


car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]','')


car_sales["Price"] = car_sales["Price"].astype(int) / 100
car_sales


car_sales["Sales Date"] = pd.date_range("1/1/2020", periods = len(car_sales))
car_sales


car_sales["Total Sales"] = car_sales["Price"].cumsum()


car_sales


# Create a scatter plot of the 'Odometer (KM)' and 'Price' column using the plot() function

#1st Method
car_sales.plot(x = 'Odometer (KM)', y = "Price", kind = 'scatter');


#2nd Method
car_sales.plot.scatter(x = 'Odometer (KM)', y = "Price");


#3rd Method (OO)
figx, axx = plt.subplots()
axx.scatter(car_sales['Odometer (KM)'], car_sales['Price'])


#Plot the total sales
car_sales.plot(x = "Sales Date", y = "Total Sales")


car_sales_1 = car_sales["Odometer (KM)"].cumsum() 
#cummalitive sum - adds every proceeding value
car_sales_1.plot()


#another way to make scatter plots
car_sales.plot(x = "Odometer (KM)", y = "Make" , kind = 'scatter')


plt.plot(car_sales['Sales Date'], car_sales['Total Sales'])


car_sales


# car_sales = car_sales.drop(["sales_data", "Totals Sales"], axis = 1)
# car_sales


x = np.random.random((10, 4))
x


#turn into a dataframe
xdf = pd.DataFrame(x, columns = ['a', 'b', 'c', 'd'])
xdf


xdf.plot(kind = 'bar')


xdf.plot.bar()


car_sales.plot(x = "Make", y = 'Odometer (KM)', kind = "bar")


car_sales.groupby(['Make']).mean()


car_sales.groupby(['Make']).mean().plot()


car_sales.groupby(['Make']).mean().plot(kind = 'bar')


temp = car_sales.groupby(['Make']).mean()
temp


temp.columns
#what is Make?
#make is not the column but the row name (equvalient to row index)


#Make is not a column so it can not be chosen as axes

#temp.plot(x = 'Make', y = 'Odometer (KM)', kind = 'bar')


car_sales["Odometer (KM)"].plot.hist(bins = 10)


car_sales["Odometer (KM)"].plot(kind = 'pie')


heart_disease = pd.read_csv("heart-disease.csv.csv")


heart_disease


heart_disease["age"].plot.hist(bins = 10);


heart_disease.plot.hist() #all values in one subplot


#create a hist of age
#all values in different subplot but one plot
heart_disease.plot.hist(subplots = True, figsize = (10, 30), bins = 25);


#boolean indexing
over_50 = heart_disease[heart_disease["age"] > 50]
over_50


# we can also use
#over_50 = heart_disease[(heart_disease["sex"] == 1) & 
#                        (heart_disease["age"] > 50)]

# or 
#     over_50 = heart_disease[(heart_disease["sex"] == 1) & 
#                             (heart_disease["target"] == 1)]


#PyPlot Method
over_50.plot.scatter(x = 'age', 
                     y = 'chol', 
                     c = 'target');


#OO Method mixed with pyplot
fig, ax = plt.subplots()
over_50.plot.scatter(x = 'age', 
                     y = 'chol', 
                     c = 'target',
                     ax = ax,
                    figsize = (10, 6));

#changes the limit of the axis
#ax.set_xlim(45, 100);
#ax.set_ylim(100, 500);


#Pure 00 Method from scratch
fig, ax = plt.subplots(figsize = (10,6))

#Plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"])

#customize the plot
ax.set(title = "Heart Disease and Cholestrol Levels",
      xlabel = "Age",
      ylabel = "Cholestrol")

#this is not correct
#ax.legend(over_50["target"], title = "Target");

#1st part looks at the handles that were used in the legend, 
#the * symmbol will use name instead of the object name

#Add a legend
ax.legend(*scatter.legend_elements(), title = "Target");

#add a horizontal line
ax.axhline(over_50["chol"].mean(),
          linestyle =  '--')


over_50.head()


#make 2 subplots in one plot
#subplot of chol, thalach and age

fig, (ax0, ax1) = plt.subplots(nrows = 2, 
                              ncols = 1,
                              figsize = (10, 10),
                              sharex = True)

#add data to ax0
scatter = ax0.scatter(x = over_50["age"],
                     y = over_50["chol"],
                     c = over_50["target"])

#customize ax0
ax0.set(title = "Heart Disease and Cholestrol Levels",
       ylabel = "Cholestrol")

#add a legen to ax0
ax0.legend(*scatter.legend_elements(), title = "Target")


#add a horizontal line
ax0.axhline(y = over_50["chol"].mean(),
            ls = '--')

############

#add data to ax1
scatter1 = ax1.scatter(x = over_50["age"],
                      y = over_50["thalach"],
                      c = over_50["target"])
#add labels
ax1.set(title = "Heart Disease and Max Heart Rate",
       xlabel = "Age",
       ylabel = "thalach")

#add legend
ax1.legend(*scatter.legend_elements(), 
           title = 'Target')

#horizontal line
ax1.axhline(over_50["thalach"].mean(),
           ls = '--');

#Title to the fig
fig.suptitle("Heart Disease Analysis", fontsize = 16, fontweight = "bold")
fig.legend(*scatter.legend_elements(), 
           title = 'Target')



# See the different styles available
plt.style.available


car_sales["Price"].plot()


#update the internal grid of matplot lib. (will not show any output)
plt.style.use('seaborn-whitegrid')


car_sales["Price"].plot()


car_sales["Price"].plot(kind = 'bar')


plt.style.use('ggplot')
car_sales['Price'].plot()


a1 = np.random.randn(10, 4)
a1


df = pd.DataFrame(a1, columns = ['a', 'b', 'c', 'd'])
df


df.plot.bar()


#customize our plot with the set() method
ax = df.plot(kind = 'bar', figsize = (10, 10))

ax.set(title = 'Random Number Graph from DataFrame',
      xlabel = 'Row Number',
      ylabel = 'Random Number')

ax.legend().set_visible(True)


#change the plot style
plt.style.use('seaborn-whitegrid')

#Pure 00 Method from scratch
fig, ax = plt.subplots(figsize = (10,6))

#Plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"], 
                    cmap = 'winter') 

#customize the plot
ax.set(title = "Heart Disease and Cholestrol Levels",
      xlabel = "Age",
      ylabel = "Cholestrol")

#Add a legend
ax.legend(*scatter.legend_elements(), title = "Target");

#1st part looks at the handles that were used in the legend, 
#the * symmbol will name instead of the object name

#add a horizontal line
ax.axhline(over_50["chol"].mean(),
          linestyle =  '--')



#change the plot style
plt.style.use('seaborn-whitegrid')

#make 2 subplots in one plot
#subplot of chol, thalach and age

fig, (ax0, ax1) = plt.subplots(nrows = 2, 
                              ncols = 1,
                              figsize = (10, 10),
                              sharex = True) 
                              
    
    
#add data to ax0
scatter0 = ax0.scatter(x = over_50["age"],
                     y = over_50["chol"],
                     c = over_50["target"],
                     cmap = 'winter')
                     # changes the colour scheme of the graph legends

#set x limits
ax0.set_xlim([50, 80])


#customize ax0
ax0.set(title = "Heart Disease and Cholestrol Levels",
       ylabel = "Cholestrol")

#add a legen to ax0
ax0.legend(*scatter.legend_elements(), title = "Target")


#add a horizontal line
ax0.axhline(y = over_50["chol"].mean(),
            ls = '--')

############

#add data to ax1
scatter1 = ax1.scatter(x = over_50["age"],
                      y = over_50["thalach"],
                      c = over_50["target"],
                      cmap = 'winter')
                      # changes the colour scheme of the graph legends

#set y limit
ax1.set_ylim([60, 200])

#add labels
ax1.set(title = "Heart Disease and Max Heart Rate",
       xlabel = "Age",
       ylabel = "Max Heart Rate")

#add legend
ax1.legend(*scatter.legend_elements(), 
           title = 'Target')

#horizontal line
ax1.axhline(over_50["thalach"].mean(),
           ls = '--', 
           label="Average");

#Title to the fig
fig.suptitle("Heart Disease Analysis", fontsize = 16, fontweight = "bold")

# this can be used to add legend in plot instead of subplots
# fig.legend(*scatter.legend_elements(), 
#            title = 'Target')



fig



fig.savefig("Heart disease analysis plot.png")



