# -*- coding: utf-8 -*-
"""
@author: fornax
"""
import os
import pandas as pd
from tqdm import tqdm


def merge_data(src_data_path, dst_data_path):
    print("Concatenating context files")
    dates = ['2008-08-22_2010-07-10', '2010-07-10_2012-05-27', '2012-05-27_2014-04-14', '2014-04-14_2016-03-01']
    contexts = ['dmop', 'evtf', 'ftl', 'saaf', 'ltdata']

    for context in tqdm(contexts):
        aggr = []
        for m_year, date in enumerate(dates):
            if m_year < 3:
                folder = os.path.join(src_data_path, 'train_set')
            else:
                folder = os.path.join(src_data_path, 'test_set')
            df = pd.read_csv(os.path.join(folder, 'context--%s--%s.csv' % (date, context)))
            aggr.append(df)
        pd.concat(aggr).to_csv(os.path.join(dst_data_path, context + '.csv'), index=False)

    # power files
    print("Concatenating power lines")
    aggr = []
    for m_year, date in enumerate(dates[:-1]):
        df = pd.read_csv(os.path.join(src_data_path, 'train_set', 'power--%s.csv' % date))
        aggr.append(df)
    pd.concat(aggr).to_csv(os.path.join(dst_data_path, 'power.csv'), index=False)
    print("Done...")
