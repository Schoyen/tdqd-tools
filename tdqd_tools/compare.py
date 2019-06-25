import numpy as np
import matplotlib.pyplot as plt


def compare_diff(data_1, data_2):
    time_points_1, vals_1 = data_1[:, 0], data_1[:, 1]
    time_points_2, vals_2 = data_2[:, 0], data_2[:, 1]

    diff = np.abs(vals_1 - vals_2)

    print(f"mean(|diff|) = {np.mean(diff)}")
    print(f"max(|diff|) = {np.max(diff)}")


def compare_plot(data_1, data_2, label_1, label_2):
    time_points_1, vals_1 = data_1[:, 0], data_1[:, 1]
    time_points_2, vals_2 = data_2[:, 0], data_2[:, 1]

    plt.plot(time_points_1, vals_1, label=label_1)
    plt.plot(time_points_2, vals_2, label=label_2)

    plt.legend(loc="best")
    plt.show()
