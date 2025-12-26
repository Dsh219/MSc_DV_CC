import pandas as pd
from plotnine import *
from mizani.breaks import date_breaks
from mizani.formatters import date_format

base_path = r"C:\Users\Shenghui\Documents\GitHub\MSc_DV_CC\Task1"

df = pd.read_csv(
    base_path + r"\data\Bitcoin_monthly_010413-011125.csv",
    sep=";"
)
df['timeOpen'] = pd.to_datetime(df['timeOpen'], utc=True).dt.to_period('M')\
                    .dt.to_timestamp().dt.strftime('%Y-%m')

#%%
# IMPORTANT: timezone-naive datetime


(
    ggplot(df, aes(x="timeOpen", y="volume"))
    + geom_line()
    + geom_point()
    + scale_y_continuous(labels=lambda l: [f"{v:.2e}" for v in l])
    + scale_x_discrete(
        labels=lambda l: [label if i % 12 == 0 else "" for i, label in enumerate(l)]
    )
    + labs(title="Bitcoin Monthly Volume", x="Month", y="Volume")
    + theme(axis_text_x=element_text(rotation=45, ha="right"))
)