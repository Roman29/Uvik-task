import pandas as pd

df = pd.read_csv (r'data.csv')

count1 = df['country'].count()

groupby_count1 = df.groupby(['country']).count()
groupby_count2 = df.groupby(["country", "person"]).first()


print ('Count of values, grouped by the Country: ' + str(groupby_count1))
print ('Country and persons from this country: ' + str(groupby_count2))