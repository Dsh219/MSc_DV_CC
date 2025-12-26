import pandas as pd
from plotnine import *
from mizani.formatters import date_format

#%%
base_path = r"C:\Users\Shenghui\Documents\GitHub\MSc_DV_CC\Task1"


#%%
# Bitcoin Monthly Volume Plot from 2013-04 to 2025-11, data source: CoinMarketCap
df = pd.read_csv(
    base_path + r"\data\Bitcoin_monthly_010413-011125.csv",
    sep=";"
)
df['timeOpen'] = pd.to_datetime(df['timeOpen'], utc=True).dt.tz_convert(None)           
df = df.sort_values('timeOpen', ascending=True).reset_index(drop=True)

(
    ggplot(df, aes(x='timeOpen', y='volume'))
    + geom_line()
    + geom_point()
    + scale_x_datetime(
        date_breaks="6 months",   # every 12 months
        labels=date_format("%Y-%m")        # show YYYY-MM
    )
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Bitcoin Monthly Volum - CoinMarketCap", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)
#%%
# Bitcoin daily Volume from 2013-04-28 to 2025-12-26, data source: CoinGecko
df = pd.read_csv(
    base_path + r"\data\btc-usd-daily_coingecko.csv"
)
df['snapped_at'] = pd.to_datetime(df['snapped_at'], utc=True).dt.tz_convert(None)           
df = df.sort_values('snapped_at', ascending=True).reset_index(drop=True)

df_monthly = df.groupby(pd.Grouper(key='snapped_at', freq='M'))['total_volume'].sum().reset_index()
df_monthly = df_monthly.iloc[:-1]

(
    ggplot(df_monthly, aes(x='snapped_at', y='total_volume'))
    + geom_line()
    + geom_point()
    + scale_x_datetime(
        date_breaks="6 months",   # every 12 months
        labels=date_format("%Y-%m")        # show YYYY-MM
    )
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Bitcoin Monthly Volume - CoinGecko", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)

#%%
# Ethereum Monthly Volume Plot from 2015-09 to 2025-11, data source: CoinMarketCap
df = pd.read_csv(
    base_path + r"\data\Ethereum_monthly_010915-011125.csv",
    sep=";"
)
df['timeOpen'] = pd.to_datetime(df['timeOpen'], utc=True).dt.tz_convert(None)             
df = df.sort_values('timeOpen', ascending=True).reset_index(drop=True)

(
    ggplot(df, aes(x='timeOpen', y='volume'))
    + geom_line()
    + geom_point()
    + scale_x_datetime(
        date_breaks="6 months",   # every 12 months
        labels=date_format("%Y-%m")        # show YYYY-MM
    )
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Ethereum Monthly Volume - CoinMarketCap", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)

#%%
# Ethereum daily Volume from 2015-08-07 to 2025-12-26, data source: CoinGecko
df = pd.read_csv(
    base_path + r"\data\eth-usd-daily_coingecko.csv"
)
df['snapped_at'] = pd.to_datetime(df['snapped_at'], utc=True).dt.tz_convert(None)           
df = df.sort_values('snapped_at', ascending=True).reset_index(drop=True)

df_monthly = df.groupby(pd.Grouper(key='snapped_at', freq='M'))['total_volume'].sum().reset_index()
df_monthly = df_monthly.iloc[:-1]

(
    ggplot(df_monthly, aes(x='snapped_at', y='total_volume'))
    + geom_line()
    + geom_point()
    + scale_x_datetime(
        date_breaks="6 months",   # every 12 months
        labels=date_format("%Y-%m")        # show YYYY-MM
    )
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Ethereum Monthly Volume - CoinGecko", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)
#%%
# Tether Monthly Volume Plot from 2013-03 to 2025-11, data source: CoinMarketCap
df = pd.read_csv(
    base_path + r"\data\Tether_monthly_010315-011125.csv",
    sep=";"
)
df['timeOpen'] = pd.to_datetime(df['timeOpen'], utc=True).dt.tz_convert(None)                
df = df.sort_values('timeOpen', ascending=True).reset_index(drop=True)

(
    ggplot(df, aes(x='timeOpen', y='volume'))
    + geom_line()
    + geom_point()
    + scale_x_datetime(
        date_breaks="6 months",   # every 12 months
        labels=date_format("%Y-%m")        # show YYYY-MM
    )
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Tether Monthly Volume - CoinMarketCap", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)

#%%
# Tether daily Volume from 2015-02-25 to 2025-12-26, data source: CoinGecko
df = pd.read_csv(
    base_path + r"\data\usdt-usd-daily_coingecko.csv"
)
df['snapped_at'] = pd.to_datetime(df['snapped_at'], utc=True).dt.tz_convert(None)           
df = df.sort_values('snapped_at', ascending=True).reset_index(drop=True)

df_monthly = df.groupby(pd.Grouper(key='snapped_at', freq='M'))['total_volume'].sum().reset_index()
df_monthly = df_monthly.iloc[:-1]

(
    ggplot(df_monthly, aes(x='snapped_at', y='total_volume'))
    + geom_line()
    + geom_point()
    + scale_x_datetime(
        date_breaks="6 months",   # every 12 months
        labels=date_format("%Y-%m")        # show YYYY-MM
    )
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + labs(title="Tether Monthly Volume - CoinGecko", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha='right'))
)
