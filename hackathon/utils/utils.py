import pandas as pd
import numpy as np


def to_datetime(df, time_col='ut_ms'):
    """
    Converts UCT timestamp [ms] to datetime in a dataframe
    """
    df[time_col] = pd.to_datetime(df[time_col], unit='ms')
    return df


def to_utms(ut):
    """
    Converts datetime to UTC timestamp [ms]
    """
    return (ut.astype(np.int64) * 1e-6).astype(int)


def align_to_power(df, powers, method='nearest'):
    """
    Aligns dataframe's time axis to a common ground
    """
    df = df.reindex(powers.index, method=method)
    if 'martian_year' in df.columns:
        df.drop(['martian_year'], axis=1, inplace=True)
    return df


def resample(df, intervals='1H'):
    """
    Resamples the data frame to a given interval
    """
    df = df.resample(intervals).mean()
    return df


def parse_data(filename, time_col='ut_ms'):
    """
    Read a dataframe and prepare the time axis
    """
    df = pd.read_csv(filename)
    df = to_datetime(df, time_col=time_col)
    df = df.set_index(time_col)
    return df


def load_dataframe(filename, intervals='1H', dropna=True):
    """
    Prepares the power data, with resampling
    """
    df = parse_data(filename)
    df = resample(df, intervals)
    if dropna:
        df = df.dropna()
    return df


def RMSE(true, pred, axis=None):
    """
    Function computes RMSE.

    :param true: expected values
    :param pred: predicted values
    :return: computed RMSE
    """
    if hasattr(true, 'values'):
        true = true.values
    if hasattr(pred, 'values'):
        pred = pred.values
    diff = true - pred
    mse = np.mean(diff ** 2, axis=axis)
    rmse = np.sqrt(mse)
    return rmse


def normalize_features(x_data, method="gaussian"):
    """
    Normalizes columns in data    
    :param x_data: input array with features in columns
    :param method: method of data normalization 
            'gaussian' - normalize data according to normal distribution, 
            'uniform' - normalize data to be in range of [0, 1], 
            'uniform_symmetric' - same but normalize to range [-1, 1] 
    :return: normalized array
    """

    eps = 0.00001

    if hasattr(x_data, 'values'):
        x_data = x_data.values

    if method == 'gaussian':

        mu = np.expand_dims(x_data.mean(0), 0)
        std = np.expand_dims(x_data.mean(0), 0)
        return (x_data - mu) / (std + eps)

    if method == 'uniform':
        max_value = np.expand_dims(x_data.max(0), 0)
        min_value = np.expand_dims(x_data.min(0), 0)
        return (x_data - min_value) / (max_value - min_value + eps)

    if method == 'uniform_symmetric':
        max_value = np.expand_dims(x_data.max(0), 0)
        min_value = np.expand_dims(x_data.min(0), 0)
        return 1 - 2*(x_data - min_value) / (max_value - min_value + eps)

