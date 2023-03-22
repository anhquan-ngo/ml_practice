```
The Nobel Prize is perhaps the world's most well known scientific award. 
Except for the honor, prestige and substantial prize money the recipient also gets a gold medal showing Alfred Nobel (1833 - 1896) who established the prize. 
Every year it's given to scientists and scholars in the categories chemistry, literature, physics, physiology or medicine, economics, and peace. 
The first Nobel Prize was handed out in 1901, and at that time the Prize was very Eurocentric and male-focused, but nowadays it's not biased in any way whatsoever. 
Surely. Right?
Well, we're going to find out! The Nobel Foundation has made a dataset available of all prize winners from the start of the prize, in 1901, to 2016. 
Let's load it in and take a look.
```

import pandas as pd
import seaborn as sns
import numpy as np
# Reading in the Nobel Prize data
nobel = pd.read_csv('datasets/nobel.csv')

# Taking a look at the first several winners
nobel.head(n=6)

# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
nobel_1901_2016 = nobel[nobel['year'].isin(list(range(1901, 2017)))]
print(len(nobel_1901_2016))

# Display the number of prizes won by male and female recipients.
print(nobel_1901_2016['sex'].value_counts())

# Display the number of prizes won by the top 10 nationalities.
print(nobel_1901_2016['birth_country'].value_counts().head(10))

# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year']/10))*10
nobel['decade'] = nobel['decade'].astype(np.int64, copy = False)
prop_usa_winners = nobel.groupby('decade', as_index = False)['usa_born_winner'].mean()

# Display the proportions of USA born winners per decade
print(prop_usa_winners)

# Setting the plotting theme
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x='decade', y='usa_born_winner', data = prop_usa_winners)

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter())

# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index = False)['female_winner'].mean()

# Plotting USA born winners with % winners on the y-axis
ax = sns.lineplot(x='decade', y='female_winner', data = prop_female_winners, hue = 'category')
ax.yaxis.set_major_formatter(PercentFormatter())

# Picking out the first woman to win a Nobel Prize
nobel[nobel['sex'] == 'Female'].nsmallest(1, 'year')

# Selecting the laureates that have received 2 or more prizes.
nobel.groupby('full_name').filter(lambda x: len(x) >= 2)

# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year

# Plotting the age of Nobel Prize winners
sns.lmplot(x='year', y='age', data = nobel)

# Same plot as above, but separate plots for each type of Nobel Prize
sns.lmplot(x='year', y='age', data = nobel, row = 'category')

# The oldest winner of a Nobel Prize as of 2016
nobel.nlargest(1, 'age')

# The youngest winner of a Nobel Prize as of 2016
nobel.nsmallest(1, 'age')


# The name of the youngest winner of the Nobel Prize as of 2016
nobel[nobel['age'] == nobel['age'].min()]['full_name'].str.split(" ", 1).tolist()[0]
