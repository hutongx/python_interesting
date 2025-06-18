import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import plotly.express as px
from typing import Any

# 读取你的 CSV 数据
df: pd.DataFrame = pd.read_csv("/Users/hutong/Code/PycharmProjects/python_interesting/data/birth_death.csv")

# 绘制交互式折线图
fig = px.line(
    df,
    x="年份",
    y=["出生人数", "死亡人数"],
    title="中国历年人口出生/死亡 (1949–2024)",
    labels={"value": "数量(百万)", "variable": "Series"},
    template="plotly_white"
)
fig.update_traces(mode="lines+markers", hovertemplate="%{y:,}")
fig.update_layout(hovermode="x unified", legend_title_text="")
fig.show()
