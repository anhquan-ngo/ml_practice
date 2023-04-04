```
Overview: Analyze two datasets on every single Lego block that has ever been built! 
This is a Pandas dataframe manipulation basic practice.
```
import pandas as pd
# Read colors data
colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows
print(colors.head)

# How many distinct colors are available?
num_colors = colors['name'].nunique()
# Print num_colors
print(num_colors)

# colors_summary: Distribution of colors based on transparency
colors_summary = colors.groupby(['is_trans']).count()

%matplotlib inline
# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets[['year','num_parts']].groupby('year').mean()

# Plot trends in average number of parts by year
parts_by_year.plot()

# themes_by_year: Number of themes shipped by year
themes_by_year = sets[['year','theme_id']].groupby('year').nunique()
print(themes_by_year.head)

num_themes = themes_by_year.loc[1999]
# Print the number of unique themes released in 1999
print(num_themes)

print("Hello")