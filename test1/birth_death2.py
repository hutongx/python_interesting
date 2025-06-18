import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import Any

# 读取数据
df: pd.DataFrame = pd.read_csv("/Users/hutong/Code/PycharmProjects/python_interesting/data/birth_death.csv")

fig, ax = plt.subplots(figsize=(12, 6))
line_births, = ax.plot([], [], label="Births", linewidth=2)
line_deaths, = ax.plot([], [], label="Deaths", linewidth=2)

ax.set_xlim(df["Year"].min(), df["Year"].max())
ax.set_ylim(0, df[["Births", "Deaths"]].values.max() * 1.05)
ax.set_title("China Annual Births and Deaths (1949–2024)")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
ax.legend()
ax.grid(True, linestyle="--", linewidth=0.5)

def init() -> None:
    line_births.set_data([], [])
    line_deaths.set_data([], [])
    return line_births, line_deaths

def animate(frame: int) -> Any:
    x = df["Year"][: frame + 1]
    line_births.set_data(x, df["Births"][: frame + 1])
    line_deaths.set_data(x, df["Deaths"][: frame + 1])
    return line_births, line_deaths

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(df),
    init_func=init,
    interval=100,  # 毫秒间隔
    blit=True
)

plt.tight_layout()
ani.save("/Users/hutong/Code/PycharmProjects/python_interesting/data/births_deaths_animation.mp4", writer="ffmpeg", dpi=200)
plt.show()
