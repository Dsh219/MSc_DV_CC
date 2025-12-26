import pandas as pd
from plotnine import *
from mizani.formatters import date_format
import country_converter as coco
cc = coco.CountryConverter()
#%%
base_path = r"C:\Users\Shenghui\Documents\GitHub\MSc_DV_CC\Task2"
mycols = ['Country Name', 'Country Code']
yr = 2013
while yr < 2025:
    mycols.append(str(yr))
    yr += 1
myrows = ['WLD','NAC','EAS','ECS','LCN','SSF','SAS','MEA']

#%%
# Deciding region and plot GDP
df = pd.read_csv(
    base_path + r"\data\GDP.csv"
)
df.isna().sum().to_csv(base_path + "./nan_GDP.csv")
df_s = df.loc[:, mycols]

# some code is not in IS03, they are below
no_IS03={}     
def convert_continent(row) -> str:
    code = row['Country Code']
    c = cc.convert(names=code, to='continent')
    if c == "not found":
        no_IS03[row['Country Name']] = code 
        return code
    else:
        return c

df_s["Country Code"] = df_s.apply(convert_continent,axis=1)

df_s = (
    df_s
    .groupby("Country Code", as_index=False)
    .sum(numeric_only=True)
)

# based on economical region, the following rows are chosen.
'''
 'World': 'WLD'
 'North America': 'NAC',
 'East Asia & Pacific': 'EAS',
 'Europe & Central Asia': 'ECS',
 'Latin America & Caribbean': 'LCN',
 'Sub-Saharan Africa': 'SSF',
             'Africa Eastern and Southern': 'AFE'
             'Africa Western and Central': 'AFW'
 'South Asia': 'SAS',            
 'Middle East, North Africa, Afghanistan & Pakistan': 'MEA',
'''


df_s = df_s[df_s['Country Code'].isin(myrows)]
df_s = df_s.reset_index(drop=True).T 
df_s = df_s.reset_index().rename(columns={'index': 'Year'})
df_s.columns = df_s.iloc[0]
df_s.rename(columns={'Country Code': 'Year'}, inplace=True)
df_s = df_s[1:]
df_s = df_s.apply(pd.to_numeric, errors='coerce')

df_long = df_s.melt(id_vars='Year', var_name='Region', value_name='GDP')
years = df_s['Year'].tolist()
(
    ggplot(df_long, aes(x='Year', y='GDP', color='Region'))
    + geom_line()
    + geom_point()
    + scale_x_continuous(breaks=years)
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="GDP for different regions", x="Year", y="GDP")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)

#%%
# debt ratio
mycols = ['Country Code']
yr = 2013
while yr < 2025:
    mycols.append(str(yr))
    yr += 1
#%%
## Debt ratio
df = pd.read_csv(
    base_path + r"\data\debt_ratio_to_gdp.csv"
)
df_s = df.loc[:, mycols]
df_s = df_s[df_s['Country Code'].isin(myrows)]

df_s = df_s.reset_index(drop=True).T 
df_s = df_s.reset_index().rename(columns={'index': 'Year'})
df_s.columns = df_s.iloc[0]
df_s.rename(columns={'Country Code': 'Year'}, inplace=True)
df_s = df_s[1:]
df_s = df_s.apply(pd.to_numeric, errors='coerce')


df_long = df_s.melt(id_vars='Year', var_name='Region', value_name='GDP')
years = df_s['Year'].tolist()
(
    ggplot(df_long, aes(x='Year', y='GDP', color='Region'))
    + geom_line()
    + geom_point()
    + scale_x_continuous(breaks=years)
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Debt:GDP ratio for different regions", x="Year", y="Debt ratio")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)

#%%
## Exchange rate is not good, since all 0 for each region
df = pd.read_csv(
    base_path + r"\data\exchange_rate.csv"
)
df_s = df.loc[:, mycols]
df_s = df_s[df_s['Country Code'].isin(myrows)]

df_s = df_s.reset_index(drop=True).T 
df_s = df_s.reset_index().rename(columns={'index': 'Year'})
df_s.columns = df_s.iloc[0]
df_s.rename(columns={'Country Code': 'Year'}, inplace=True)
df_s = df_s[1:]
df_s = df_s.apply(pd.to_numeric, errors='coerce')


df_long = df_s.melt(id_vars='Year', var_name='Region', value_name='GDP')
years = df_s['Year'].tolist()
(
    ggplot(df_long, aes(x='Year', y='GDP', color='Region'))
    + geom_line()
    + geom_point()
    + scale_x_continuous(breaks=years)
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Exchange rate for different regions", x="Year", y="Rate")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)

#%%
## Inflation
df = pd.read_csv(
    base_path + r"\data\inflation.csv"
)
df_s = df.loc[:, mycols]
df_s = df_s[df_s['Country Code'].isin(myrows)]

df_s = df_s.reset_index(drop=True).T 
df_s = df_s.reset_index().rename(columns={'index': 'Year'})
df_s.columns = df_s.iloc[0]
df_s.rename(columns={'Country Code': 'Year'}, inplace=True)
df_s = df_s[1:]
df_s = df_s.apply(pd.to_numeric, errors='coerce')


df_long = df_s.melt(id_vars='Year', var_name='Region', value_name='GDP')
years = df_s['Year'].tolist()
(
    ggplot(df_long, aes(x='Year', y='GDP', color='Region'))
    + geom_line()
    + geom_point()
    + scale_x_continuous(breaks=years)
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Inflation for different regions", x="Year", y="Inflation")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)
#%%
## interest rate            not suitable on region level
df = pd.read_csv(
    base_path + r"\data\real_interest_rate.csv"
)
df_s = df.loc[:, mycols]
df_s = df_s[df_s['Country Code'].isin(myrows)]

df_s = df_s.reset_index(drop=True).T 
df_s = df_s.reset_index().rename(columns={'index': 'Year'})
df_s.columns = df_s.iloc[0]
df_s.rename(columns={'Country Code': 'Year'}, inplace=True)
df_s = df_s[1:]
df_s = df_s.apply(pd.to_numeric, errors='coerce')


df_long = df_s.melt(id_vars='Year', var_name='Region', value_name='GDP')
years = df_s['Year'].tolist()
(
    ggplot(df_long, aes(x='Year', y='GDP', color='Region'))
    + geom_line()
    + geom_point()
    + scale_x_continuous(breaks=years)
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Inflation for different regions", x="Year", y="Inflation")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)
#%%
## unemployment
df = pd.read_csv(
    base_path + r"\data\unemployment.csv"
)
df_s = df.loc[:, mycols]
df_s = df_s[df_s['Country Code'].isin(myrows)]

df_s = df_s.reset_index(drop=True).T 
df_s = df_s.reset_index().rename(columns={'index': 'Year'})
df_s.columns = df_s.iloc[0]
df_s.rename(columns={'Country Code': 'Year'}, inplace=True)
df_s = df_s[1:]
df_s = df_s.apply(pd.to_numeric, errors='coerce')


df_long = df_s.melt(id_vars='Year', var_name='Region', value_name='GDP')
years = df_s['Year'].tolist()
(
    ggplot(df_long, aes(x='Year', y='GDP', color='Region'))
    + geom_line()
    + geom_point()
    + scale_x_continuous(breaks=years)
    + labs(title="Unemployment for different regions", x="Year", y="Unemployment rate %")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)