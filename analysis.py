import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

df1 = pd.read_csv('Online Table.csv')
df2 = pd.read_csv('Inperson Table.csv')
df = pd.merge(df1,df2, how='outer')
pd.set_option('display.max_columns', None)
df.astype(str)
# Changing column names
df.rename(columns={'Question 2': 'Age',
                   'Online Table': 'Participant',
                   'Question 5': 'Zip Code'}, inplace=True)

# Adding all the options column to get a binary number
df['Gender'] = df['Question 3'] + df['Unnamed: 3'] + df['Unnamed: 4']
df['Degree of Edu'] = df['Question 6'] + df['Unnamed: 13'] + df['Unnamed: 14'] + df['Unnamed: 15'] \
                      + df['Unnamed: 16'] + df['Unnamed: 17'] + df['Unnamed: 18'] + df['Unnamed: 19']
df['Income'] = df['Question 7'] + df['Unnamed: 21'] + df['Unnamed: 22'] + df['Unnamed: 23'] \
               + df['Unnamed: 24']
df['Health Condition'] = df['Question 8'] + df['Unnamed: 26'] + df['Unnamed: 27'] + df['Unnamed: 28']
df['Outdoor Activity Engaged'] = df['Question 10'] + df['Unnamed: 44'] + df['Unnamed: 45'] + df['Unnamed: 4'] + \
                                 df['Unnamed: 47'] + df['Unnamed: 48']
df['Outdoor Activity Eliminated(Days)'] = df['Question 16'] + df['Unnamed: 78'] + df['Unnamed: 79'] + df[
    'Unnamed: 80'] + df['Unnamed: 81'] + df['Unnamed: 82']
df['Air Index (Activity Reduced)'] = df['Question 17'] + df['Unnamed: 84'] + df['Unnamed: 85'] + df['Unnamed: 86'] + \
                                     df['Unnamed: 87'] + df['Unnamed: 88'] + df['Unnamed: 89']
df['Air Index(Activity Eliminated)'] = df['Question 18'] + df['Unnamed: 91'] + df['Unnamed: 92'] + df['Unnamed: 93'] + \
                                       df['Unnamed: 94'] + df['Unnamed: 95'] + df['Unnamed: 96']

# Filtering rows
df = df.filter(['Age', 'Gender',
                'Degree of Edu', 'Income',
                'Health Condition',
                'Outdoor Activity Engaged',
                'Outdoor Activity Eliminated(Days)',
                'Air Index (Activity Reduced)',
                'Air Index(Activity Eliminated)'
                ])

df = df.drop(df.index[0])
df = df.dropna()

# Changing values to responses
df["Gender"] = df["Gender"].replace({'100': 'Male', '010': 'Female', '001': 'Others', '000': 'Others'})

df['Degree of Edu'] = df['Degree of Edu'].replace({'00000000': 'No Response',
                                                   '10000000': '8th grade or less',
                                                   '01000000': 'High school',
                                                   '00100000': 'High school graduate',
                                                   '00010000': 'College',
                                                   '00001000': 'Associates degree',
                                                   '00000100': 'Bachelor’s degree',
                                                   '00000010': 'Master’s degree',
                                                   '00000001': 'Ph.D'})

df['Income'] = df['Income'].replace({'00000': 'No Response',
                                     '10000': '$25,000 or less',
                                     '01000': 'Upto to $49,999',
                                     '00100': 'Upto to $74,999',
                                     '00010': 'Upto to $99,999',
                                     '00001': '$100,000 or more',
                                     })
df['Health Condition'] = df['Health Condition'].replace({'00000': 'No Response',
                                                         '1000': 'Excellent',
                                                         '0100': 'Good',
                                                         '0010': 'Fair',
                                                         '0001': 'Poor',
                                                         })
df['Outdoor Activity Engaged'] = df['Outdoor Activity Engaged'].replace({'000000': 'No Response',
                                                                         '100000': 'Daily',
                                                                         '010000': 'A few times per week',
                                                                         '001000': 'Once per week',
                                                                         '000100': 'once per month',
                                                                         '000001': 'Rarely',
                                                                         '000010': 'Common'
                                                                         })
df['Outdoor Activity Eliminated(Days)'] = df['Outdoor Activity Eliminated(Days)'].replace({'000000': 'No Response',
                                                                                           '100000': '1',
                                                                                           '010000': '2',
                                                                                           '001000': '3',
                                                                                           '000100': '4',
                                                                                           '000010': '5',
                                                                                           '000001': '6'
                                                                                           })
df['Air Index (Activity Reduced)'] = df['Air Index (Activity Reduced)'].replace({'0000000': 'No Response',
                                                                                 '1000000': 'Green – Good',
                                                                                 '0100000': 'Yellow – Moderate',
                                                                                 '0010000': 'Orange – Unhealthy for Sensitive Groups',
                                                                                 '0001000': 'Red – Unhealthy',
                                                                                 '0000100': 'Purple – Very Unhealthy',
                                                                                 '0000010': 'Maroon – Hazardous',
                                                                                 '0000001': 'Not familiar'
                                                                                 })
df['Air Index(Activity Eliminated)'] = df['Air Index(Activity Eliminated)'].replace({'0000000': 'No Response',
                                                                                     '1000000': 'Green – Good',
                                                                                     '0100000': 'Yellow – Moderate',
                                                                                     '0010000': 'Orange – Unhealthy for Sensitive Groups',
                                                                                     '0001000': 'Red – Unhealthy',
                                                                                     '0000100': 'Purple – Very Unhealthy',
                                                                                     '0000010': 'Maroon – Hazardous',
                                                                                     '0000001': 'Not familiar'
                                                                                     })
df.reset_index()

sns.set_theme()
# Plotting of Income range
income = df.Income.value_counts()
ax = plt.figure(figsize=(10, 5))
ax = sns.barplot(x=income.index, y=income)
ax.set(xlabel='Income Range', ylabel='Count', title='Income range of Participants')

# Plotting of participants age
age = df.Age.reset_index()
age.sort_values(by='Age', inplace=True, ascending=True)
age.reset_index()
ax1 = plt.figure(figsize=(12, 6))
sns.set_style('ticks')
sns.set_style('whitegrid')
ax1 = sns.histplot(age.Age, binwidth=5, color='g')
ax1.set(title='Age of participants')
plt.xticks(rotation=90)

# Plotting of gender
gender = df.Gender.value_counts()
sns.set_style('dark')
ax2 = plt.figure(figsize=(6, 5))
ax2 = plt.pie(gender, labels=gender.index, colors=['r', 'b', 'g'],autopct='%1.1f%%')
plt.title('Gender of participants')

# Plotting of Air Index(Activity Eliminated)
act = df['Air Index(Activity Eliminated)'].value_counts()
sns.set_style('ticks')
sns.set_style('darkgrid')
ax3 = plt.figure(figsize=(10, 5))
ax3 = plt.barh(y=act.index, width=act)
plt.title('Air Index(Activity Eliminated)')
ax3[0].set_color('red')
ax3[1].set_color('purple')
ax3[2].set_color('orange')
ax3[3].set_color('maroon')
ax3[4].set_color('black')
ax3[6].set_color('yellow')

plt.tight_layout()
plt.show()

#save file to csv
df.to_csv('analysis.csv')

