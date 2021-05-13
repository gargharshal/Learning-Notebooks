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


# in general the above method of resizing 
# works for all but not for lmplot and joinplot
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


stats_df = df.drop(["Total", "Stage", "Legendary"], axis = 1)
stats_df[stats_df['Name'].isin(['Bulbasaur', 'Charmander'])]


melted_df = pd.melt(stats_df, 
                    ["Name", "Type 1", "Type 2"], 
                    var_name="Stat")
melted_df[melted_df['Name'].isin(['Bulbasaur', 'Charmander'])]


plt.figure(figsize=(12, 8))
sns.stripplot(x = 'Stat', y = 'value', 
              data = melted_df, hue  = 'Type 1',
             dodge = True); # dots doesn't overlap
plt.ylim(0, 200)
plt.legend(loc = 2, #shifts the legend in upper left corner
           bbox_to_anchor=(1, 1)) # Shifts the legend outside


plt.figure(figsize=(24, 6))
g = sns.catplot(x = 'Type 1',
              y = 'Attack',
              data = df,
              col = 'Stage', #seperated by Stage (category)
              kind = 'swarm', #type of graph in it
           hue = "Type 2"); #legend color

#rotate the axis
g.set_xticklabels(rotation = -45);


#calculate correlations
corr = stats_df.corr()
corr


#create heatmap
sns.heatmap(corr);


sns.set_style('white')


sns.displot(x = 'Attack', 
            kind = 'kde', # this adds the estimation curve 
            hue = 'Stage',
            data = df,
            palette = 'light:#5A9')


# histogram and kde
sns.displot(x = 'Attack', 
            kde = True, # this adds the estimation curve 
            bins = 10,
            data = df)


# Density Plot
plt.figure(figsize=(8, 8));

sns.displot(x = 'Attack', y = 'Defense', data = df)

plt.xlim(0, 150)
plt.ylim(0, 150)


# Density Plot
plt.figure(figsize=(8, 8));

sns.displot(x = 'Attack', y = 'Defense', 
            kind = 'kde', data = df,
           rug = True) #draw a dash mark for every point on a univariate distribution.

plt.xlim(0, 150)
plt.ylim(0, 150)


sns.jointplot(x='Attack', y='Defense', data=df)


sns.jointplot(x='Attack', y='Defense', 
              hue = 'Stage', data=df,
             xlim = (0, 150),
             ylim = (0, 200),
             palette = 'light:#5A9')


# Various kind paramaters scatter , reg, resid, kde, hex
sns.jointplot(x='total_bill',y='tip',data=tips, kind='scatter')


sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde')


sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')


sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')


sns.pairplot(tips, hue= 'sex', palette = 'winter')
