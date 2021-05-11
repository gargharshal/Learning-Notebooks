import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic("matplotlib", " inline")


get_ipython().run_cell_magic("time", " ", """df = pd.read_csv('Pokemon.csv')
df.drop(['#'], axis = 1, inplace = True)
df.head()""")


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
           fit_reg = False,
           height = 5, aspect = 2); # alternative to chnage figsize



