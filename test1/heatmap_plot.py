import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def heatmap_plot() -> None:
    """
    reference: https://x.com/clcoding/status/1931132748187775241
    :return:
    """
    data = np.random.rand(10, 12)
    # data = np.random.rand(12, 24)
    sns.heatmap(data, cmap='Reds')
    plt.show()
    # source code -- clcoding.com


if __name__ == '__main__':
    heatmap_plot()
