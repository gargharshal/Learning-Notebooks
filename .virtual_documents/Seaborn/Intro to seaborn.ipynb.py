import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


import numpy as np


df = pd.read_csv("Pokemon.csv", encoding="unicode_escape")
df = df.drop(["#"], axis = 1)


df.head()


df.info()


df["Type 1"].unique()


df["Type 2"].unique()


sns.lmplot("Attack", "Defense", data = df)


sns.lmplot("Attack", 
          "Defense", 
          data = df,
          fit_reg = False,
          hue = 'Stage')


sns.lmplot("Attack", 
          "Defense", 
          data = df,
          fit_reg = False,
          hue = 'Stage')

#for extra function we need to use matplotlib

plt.xlim(0, None)
plt.ylim(0, None)


sns.boxplot(data = df)


#dropping total, Stage and Legendary 
stats_df = df.drop(["Total", "Stage", "Legendary"], axis = 1)

plt.figure(figsize=(10, 6))
sns.boxplot(data = stats_df)


x = np.random.randn(10000)
sns.boxplot(x)



plt.hist(x, bins = 200);


sns.violinplot(x)


#sample plot

tips = sns.load_dataset("tips")
ax = sns.violinplot(x="sex", y="tip", data=tips)
ax.set_title('Distribution of tips', fontsize=16);


plt.figure(figsize = (10, 6))
ax = sns.violinplot(x="day", y="total_bill", hue="sex", data=tips)
ax.set_title('Distribution of total bill amount per day', fontsize=16);


# Set theme
sns.set_style('whitegrid')
plt.figure (figsize = (10, 6))
# Violin plot
sns.violinplot(x='Type 1', y='Attack', data=df);


# Set the color palette

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]


# Set theme
sns.set_style('whitegrid')
plt.figure (figsize = (10, 6))
# Violin plot
sns.violinplot(x='Type 1', y='Attack', data=df, palette=pkmn_type_colors);


tips.head()


plt.figure(figsize=(10,6))
plt.title('Attack by Type')

sns.swarmplot(x = 'Type 1', y = 'Attack', data = df, color="black", 
             alpha = 0.7); #make it transparent


plt.figure(figsize=(10,6))
plt.title('Attack by Type')

sns.violinplot(x = 'Type 1', y = 'Attack', data = df, inner = None, palatte = pkmn_type_colors)

sns.swarmplot(x = 'Type 1', y = 'Attack', data = df, color="black", 
             alpha = 0.7); #make it transparent


stats_df.head()


melted_df = pd.melt(stats_df, 
                    ["Name", "Type 1", "Type 2"], 
                    var_name="Stat")
melted_df


#shape of the normal vs melted
stats_df.shape, melted_df.shape


sns.swarmplot(x = 'Stat', y = 'value', data = melted_df, hue = 'Type 1');


#improve the previous plot
plt.figure(figsize=(15, 9))

sns.swarmplot(x = 'Stat',
             y = 'value',
             data = melted_df,
             hue = "Type 1",
             dodge = True, #seperate points by hue
             palette = pkmn_type_colors)

plt.ylim(0, 260)
plt.legend(loc = 2, #shifts the legend in upper left corner
           bbox_to_anchor=(1, 1)) # Shifts the legend outside


#calculate correlations
corr = stats_df.corr()

#create heatmap
sns.heatmap(corr);



#Histogram

sns.distplot(df.Attack)


#bar plot
sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)
 
# Rotate x-labels
plt.xticks(rotation=-45)


plt.figure(figsize=(24, 6))
g = sns.catplot(x = 'Type 1',
              y = 'Attack',
              data = df,
              col = 'Stage', #seperated by Stage (category)
              kind = 'swarm', #type of graph in it
           hue = "Type 2"); #legend color

#rotate the axis
g.set_xticklabels(rotation = -45);


# Density Plot
plt.figure(figsize=(8, 8));

sns.kdeplot(df.Attack, df.Defense)

plt.xlim(0, 140)
plt.ylim(0, 140)


sns.jointplot(x='Attack', y='Defense', data=df)
