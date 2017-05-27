import matplotlib.pyplot as plt

from hackathon.utils.utils import RMSE


def compare_rmse_on_lines(y_true, y_pred, col_names):
    rmse = RMSE(y_true, y_pred, axis=0)
    fig = plt.figure(figsize=(20, 2))
    ax = plt.subplot(1, 1, 1)
    plt.plot(rmse, 'o-')
    _ = ax.set_xticklabels(col_names)

    return sorted(zip(rmse, col_names), reverse=True)
