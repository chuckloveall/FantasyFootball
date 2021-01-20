import pandas as pd #import pandas in to our code so we can use it

csv_path = '2019.csv' #our file path is just our file name

df = pd.read_csv(csv_path) #load our CSV in to a DataFrame using read_csv

df.head() # view the first 5 rows of our DataFrame
print(df.shape) # shape is an attribute that tells us the shape of our DataFrame in the format (rows, columns)
print('We have', df.shape[0], 'players we can analyze for the 2019 season')
print('We have', df.shape[1], 'columns of data we can analyze for the 2019 season')

#This is what you should see as your output:
# (620, 28)
# We have 620 players we can analyze for the 2019 season
# We have 28 columns of data we can analyze for the 2019 season
# __class__ is an attribute that tells us what class an object belongs to
# you can see here, our df object belongs to the DataFrame class located within pandas
df.__class__
#This is what you should see as your output:
# pandas.core.frame.DataFrame
df.columns # columns is an attribute that shows us our DataFrames' columns

# This is what you should see as your output:
# Index(['Unnamed: 0', 'Player', 'Tm', 'Pos', 'Age', 'G', 'GS', 'Cmp', 'Att',
#        'Yds', 'Int', 'Att.1', 'Yds.1', 'Tgt', 'Rec', 'Yds.2', 'Y/R', 'Fumbles',
#        'FumblesLost', 'PassingYds', 'PassingTD', 'PassingAtt', 'RushingYds',
#        'RushingTD', 'RushingAtt', 'ReceivingYds', 'ReceivingTD',
#        'FantasyPoints'],
#       dtype='object')
df.head() #show us the first five rows of our DataFrame
