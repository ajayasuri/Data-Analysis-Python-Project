#=======================================================================================================================================
# Import libraries and dataframe
#=======================================================================================================================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib

# Import dataframe
df = pd.read_csv('Occupations by Share.csv')

# Statistical summary and exploration
df.shape
df.columns
df.head()

# Additional exploration
df.Year.value_counts()
df['Broad Occupation'].value_counts().size
df['Broad Occupation'].value_counts()
df['Detailed Occupation'].value_counts().size
df['Total Population'].value_counts().size
df['Average Wage'].value_counts().size

#=======================================================================================================================================
# Data cleaning
#=======================================================================================================================================

# Drop columns that we do not need
df = df.drop(['ID Major Occupation Group', 'ID Minor Occupation Group', 'ID Broad Occupation', 'ID Detailed Occupation',
        'ID Year', 'ID Workforce Status',  'Workforce Status',  'Slug Detailed Occupation', 'ID PUMS Industry',
       'Slug PUMS Industry', 'ID Industry Sector', 'Record Count', 'PUMS Industry', 'Industry Sector', 'Slug Industry Sector'], axis=1)
# Exclude more columns that can not be utilized due to time constraint
df = df.drop(['Major Occupation Group', 'Minor Occupation Group', 'Detailed Occupation'], axis=1)

#=======================================================================================================================================
# Reorganize and extract data
#=======================================================================================================================================

# Group data by 'Broad Occupation' and compute the average mean
df = df.groupby(['Broad Occupation', 'Year']).mean().reset_index()
# Find min and max for 'Total Population' and 'Average Wage
df.iloc[df['Total Population'].argmax()]
df.iloc[df['Average Wage'].argmax()]
df.iloc[df['Total Population'].argmin()]
df.iloc[df['Average Wage'].argmin()]

#=======================================================================================================================================
# Explorating Data Vizualization with matplotlib
#=======================================================================================================================================

# Total Population change over time
for title, group in df.groupby('Broad Occupation'):
    group.plot(x='Year', y='Total Population', kind='bar', title=title)
# Average Wage change over time
for title, group in df.groupby('Broad Occupation'):
    group.plot(x='Year', y='Average Wage', kind='bar', title=title)
# Total Population/Average Wage Combined Chart
for title, group in df.groupby('Broad Occupation'):
    group.plot(x='Year', y=['Total Population','Average Wage'], kind='bar', title=title)
# Correlation chart between Total Population and Average Wage
for title, group in df.groupby('Broad Occupation'):
    group.plot(x='Average Wage', y='Total Population', kind='scatter', title=title)