import matplotlib.pyplot as plt
import pandas as pd


def benchmark_model(model, y_col_names, num_worst_columns=6, plot_rmse=False, ax=None):

    valid_rmse_per_line = model.eval_info['valid_rmse_per_line']
    sdata = sorted(zip(y_col_names, valid_rmse_per_line), key=lambda x: x[1], reverse=True)[:num_worst_columns]

    data = {c: d for c, d in sdata}
    data['train_rmse'] = model.eval_info['train_rmse']
    data['valid_rmse'] = model.eval_info['valid_rmse']
    df = pd.DataFrame(data=data, index=[model.eval_info['name']])
    df['info'] = model.eval_info['info']

    if plot_rmse:
        if ax is None:
            fig = plt.figure(figsize=(20, 2))
            ax = plt.subplot(1, 1, 1)

        ax.plot(valid_rmse_per_line, 'o-')
        _ = ax.set_xticklabels(y_col_names)

    return df


def benchmark_models(models, y_columns):
    dfs = []
    for model in models.items():
        df = benchmark_model(model[1], y_col_names=y_columns, plot_rmse=False)
        dfs.append(df)

    return pd.concat(dfs)