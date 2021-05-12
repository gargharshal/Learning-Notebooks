import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic("matplotlib", " inline")


df = pd.read_csv('https://raw.githubusercontent.com/gargharshal/Learning-Notebooks/master/Seaborn/Pokemon.csv', 
                 encoding="unicode_escape")
df.drop(['#'], axis = 1, inplace = True)
df.head()


df.info()


df['Type 1'].unique(), df['Type 2'].unique()


# sns.lmplot(x = df['Attack'], y = df['Defense']) # dosen't work
fig, ax = plt.subplots(figsize = (10, 5))
sns.regplot(x = 'Attack', y = 'Defense', 
            data = df, 
            ax = ax,
            fit_reg = True); # This will create the regression line


# in general the above method works for all but not for lmplot and joinplot
sns.lmplot(x = 'Attack', y = 'Defense', data = df, 
           hue = 'Stage', # define subsets of the data           
           fit_reg = False, #this would have created 3 reg lines
           height = 5, aspect = 2); # alternative to chnage figsize


sns.boxplot(data = df);


# for a better visual, remove the extremes
sns.boxplot(data = df.drop(['Total', 'Stage', 'Legendary'], axis = 1));


tips = sns.load_dataset("tips")
plt.figure(figsize = (10, 6))
ax = sns.violinplot(x="day", y="total_bill", hue="sex", data=tips)
ax.set_title('Distribution of total bill amount per day', fontsize=16);


tips = sns.load_dataset("tips")
plt.figure(figsize = (10, 6))
ax = sns.violinplot(x="day", y="total_bill", 
                    hue="sex", data=tips,
                   split = True) # this will create 
ax.set_title('Distribution of total bill amount per day', fontsize=16);


plt.figure(figsize=(12,6))
plt.title('Attack by Type')

sns.swarmplot(x = 'Type 1', y = 'Attack', data = df); #make it transparent


plt.figure(figsize=(12,6))
plt.title('Attack by Type')

sns.swarmplot(x = 'Type 1', y = 'Attack', data = df, color = 'black', 
             alpha = 0.7); #make it transparent
sns.boxplot(x = 'Type 1', y = 'Attack', data = df)



