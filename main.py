import pandas as pd

df=pd.read_csv('customer_shopping_behavior.csv')
print(df.head())#give top 5 rows
print(df.info())#give column wise data for all cols
print(df.describe(include='all')) # provide mean median count and many more for data
print(df.isnull().sum())# checks for any data present as null

#filling empty review rating with median of each category
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x : x.fillna(x.median()))
print(df.isnull().sum())

#converting columns name in snake casing
df.columns=df.columns.str.lower().str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

#create a column age_group
labels=['young_adult','adult','mid_aged','senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(10))

#create column purchase_frequency_days
ferquency_days={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(ferquency_days)
print(df[['frequency_of_purchases','purchase_frequency_days']])
print(df.isnull().sum())

#checking discount_appied and promo_code_used are same or not
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied']==df['promo_code_used']).all())
df=df.drop('promo_code_used',axis=1)
print(df.columns)

df=df.to_csv('pandas_customer_shopping_behavior.csv',index=False)
