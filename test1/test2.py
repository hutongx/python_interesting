# sketch.py
from p5 import setup, draw, size, background, stroke, point, mag, sin, cos, atan2, PI, run

# 全局时间
t = 0.0

def setup():
    size(400, 400)
    background(9)

def draw():
    global t
    background(9)
    stroke(255, 66)  # 白色 + alpha=66
    t += PI / 45     # 时间步长和 p5.js 里一样

    for i in range(10000, 0, -1):
        x = i % 200
        y = i / 55.0

        # —— 正是你给的那套数学公式 ——
        k = 9 * cos(x / 8.0)
        e = y / 8.0 - 12.5
        d = (mag(k, e) ** 2) / 99 + sin(t) / 6 + 0.5

        q = (
            99
            - e * sin(atan2(k, e) * 7) / d
            + k * (3 + cos(d * d - t) * 2)
        )
        c = d / 2 + e / 69 - t / 16

        px = q * sin(c) + 200
        py = (q + 19 * d) * cos(c) + 200

        point(px, py)

if __name__ == '__main__':
    run()



# import matplotlib  # type: ignore
# matplotlib.use('TkAgg')  # 或者 'Qt5Agg'
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# def update(frame):
#     global t
#     t += np.pi / 45
#
#     xs = []
#     ys = []
#     for i in range(10000, 0, -1):
#         x = i % 200
#         y = i / 55.0
#
#         k = 9 * np.cos(x / 8.0)
#         e = y / 8.0 - 12.5
#         d = (np.hypot(k, e) ** 2) / 99 + np.sin(t) / 6 + 0.5
#
#         q = (99
#              - e * np.sin(np.arctan2(k, e) * 7) / d
#              + k * (3 + np.cos(d * d - t) * 2)
#             )
#         c = d / 2 + e / 69 - t / 16
#
#         px = q * np.sin(c) + 200
#         py = (q + 19 * d) * np.cos(c) + 200
#
#         xs.append(px)
#         ys.append(py)
#
#     scat.set_offsets(np.column_stack((xs, ys)))
#     scat.set_color((1,1,1,66/255))  # 白色+alpha
#     return scat,
#
#
# if __name__ == '__main__':
#     # 全局时间
#     t = 0.0
#
#     # 初始化 figure & scatter
#     fig, ax = plt.subplots(figsize=(4, 4))
#     scat = ax.scatter([], [], s=1)
#     ax.set_xlim(0, 400)
#     ax.set_ylim(0, 400)
#     ax.set_facecolor((9 / 255, 9 / 255, 9 / 255))
#
#     ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
#     plt.show()