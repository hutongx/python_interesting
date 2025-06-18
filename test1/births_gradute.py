import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
from typing import List

# Ensure Plotly opens in your browser
pio.renderers.default = "browser"

# 1. Known data
births_known_years: List[int] = list(range(2000, 2025))
births_known: List[float] = [
    17.71, 17.02, 16.47, 15.99, 15.93, 16.17, 15.85, 15.94, 16.08, 15.91,
    15.92, 17.97, 19.73, 17.76, 18.97, 16.55, 17.86, 17.23, 15.23, 14.65,
    12.02, 10.62, 9.56, 9.02, 9.54
]  # in millions

grads_known_years: List[int] = list(range(2010, 2026))
grads_known: List[float] = [
    6.30, 6.60, 6.80, 6.99, 7.27, 7.49, 7.65, 7.95,
    8.20, 8.34, 8.74, 9.09, 10.76, 11.58, 11.79, 12.22
]  # in millions

# 2. Fit linear trend models
coef_births: np.ndarray = np.polyfit(births_known_years, births_known, 1)
coef_grads: np.ndarray = np.polyfit(grads_known_years, grads_known, 1)


def predict_linear(year: int, coef: np.ndarray) -> float:
    """Predict value at given year using linear coefficients [slope, intercept]."""
    slope, intercept = coef
    return slope * year + intercept


# 3. Build full dataset 2000–2050
years: List[int] = list(range(2000, 2051))
births: List[float] = []
graduates: List[float] = []

for y in years:
    if y in births_known_years:
        births.append(births_known[births_known_years.index(y)])
    else:
        births.append(round(predict_linear(y, coef_births), 2))

    if y in grads_known_years:
        graduates.append(grads_known[grads_known_years.index(y)])
    else:
        graduates.append(round(predict_linear(y, coef_grads), 2))

df: pd.DataFrame = pd.DataFrame({
    "Year": years,
    "Births (millions)": births,
    "Graduates (millions)": graduates
})

# 4. Plot interactive chart
fig = px.line(
    df,
    x="Year",
    y=["Births (millions)", "Graduates (millions)"],
    title="China Annual Births & University Graduates (2000–2050)",
    labels={"value": "Count (millions)", "variable": "Series"},
    template="plotly_white"
)
fig.update_traces(mode="lines+markers", hovertemplate="%{y:.2f} million")
fig.update_layout(hovermode="x unified", legend_title_text="Series")

# 5. Save and show
fig.write_html("births_graduates_2000_2050.html", include_plotlyjs="cdn")
fig.show()
