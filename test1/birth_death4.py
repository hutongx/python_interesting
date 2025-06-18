import plotly.io as pio
# 渲染器可选 'browser'（默认系统浏览器）、'iframe'、'jupyterlab' 等
pio.renderers.default = "browser"
import pandas as pd
import plotly.express as px

# 1. 读入数据
df = pd.read_csv("/Users/hutong/Code/PycharmProjects/python_interesting/data/birth_death.csv")

# 2. 绘图
fig = px.line(
    df,
    x="Year",
    y=["Births", "Deaths"],
    title="China Annual Births and Deaths (1949–2024)",
    labels={"value": "Count", "variable": "Series"},
    template="plotly_white"
)
fig.update_traces(mode="lines+markers", hovertemplate="%{y:,}")
fig.update_layout(hovermode="x unified", legend_title_text="")

# 3. 弹出默认浏览器窗口显示
fig.show()
