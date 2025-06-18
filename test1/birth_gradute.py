import matplotlib
matplotlib.use('TkAgg')
#!/usr/bin/env python3
from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main() -> None:
    # 1. 已知的出生数据（单位：百万）
    births_known_years: List[int] = list(range(2000, 2025))
    births_known: List[float] = [
        17.71, 17.02, 16.47, 15.99, 15.93,
        16.17, 15.85, 15.94, 16.08, 15.91,
        15.92, 17.97, 19.73, 17.76, 18.97,
        16.55, 17.86, 17.23, 15.23, 14.65,
        12.02, 10.62, 9.56, 9.02, 9.54
    ]

    # 2. 已知的大学毕业生数据（单位：百万）
    grads_known_years: List[int] = list(range(2010, 2026))
    grads_known: List[float] = [
        6.30, 6.60, 6.80, 6.99, 7.27,
        7.49, 7.65, 7.95, 8.20, 8.34,
        8.74, 9.09, 10.76, 11.58, 11.79,
        12.22
    ]

    # 3. 用线性回归拟合趋势，用于预测缺失年份
    coef_births: np.ndarray = np.polyfit(births_known_years, births_known, 1)
    coef_grads: np.ndarray = np.polyfit(grads_known_years, grads_known, 1)

    def predict(year: int, coef: np.ndarray) -> float:
        """线性预测函数，返回保留两位小数的预测值。"""
        slope, intercept = coef
        return round(slope * year + intercept, 2)

    # 4. 构建2000–2050完整数据
    years: List[int] = list(range(2000, 2051))
    births: List[float] = []
    graduates: List[float] = []

    for y in years:
        if y in births_known_years:
            births.append(births_known[births_known_years.index(y)])
        else:
            births.append(predict(y, coef_births))

        if y in grads_known_years:
            graduates.append(grads_known[grads_known_years.index(y)])
        else:
            graduates.append(predict(y, coef_grads))

    # 5. 转为DataFrame并打印
    df: pd.DataFrame = pd.DataFrame({
        "Year": years,
        "Births_millions": births,
        "Graduates_millions": graduates
    })
    print(df.to_string(index=False))

    # 6. 绘图
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["Year"], df["Births_millions"], label="Births", linewidth=2)
    ax.plot(df["Year"], df["Graduates_millions"], label="Graduates", linewidth=2)
    ax.set_title("China Annual Births & University Graduates (2000–2050)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Count (millions)")
    ax.legend()
    ax.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
