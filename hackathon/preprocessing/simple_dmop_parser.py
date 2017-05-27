"""
Extract subsystem command counts per hour
"""
import os
from datetime import datetime
import pandas as pd
from hackathon.utils.utils import to_datetime, to_utms


def read_dmop(dmop_data_path):
    """
    Function to read a csv file and resample to hourly 
    """
    df = pd.read_csv(dmop_data_path)
    df = to_datetime(df)
    df = df.set_index('ut_ms')
    return df


def generate_count(grouper, name, dmop_data):
    """
    Generate group statistics per hour     
    """
    print "Generating dmop counts:" + name

    dmop_data['grp'] = dmop_data.index.map(grouper)
    dmop_hour = dmop_data.groupby(['grp', 'device']).count()
    dmop_hour = dmop_hour.reset_index().pivot(columns='device', index='grp', values='cmd').fillna(0)
    dmop_hour['sum'] = dmop_hour.sum(axis=1)
    dmop_hour.columns = ['dmop_count_' + name + '_' + str(i) for i in dmop_hour.columns]
    dmop_hour.index.names = ['ut_ms']
    dmop_hour.index = to_utms(dmop_hour.index)
    return dmop_hour


def simple_parser(data_path, dst_data_path, save_postfix=''):
    """
    Simple dmop parser
    """
    print "Running simple dmop parser"

    dmop_df = read_dmop(data_path)
    # Extract device and cmd code from subsystem
    dmop_df = dmop_df[dmop_df['subsystem'].str.startswith('A')]
    dmop_df['device'] = dmop_df['subsystem'].map(lambda x: x[0:4])
    dmop_df['cmd'] = dmop_df['subsystem'].map(lambda x: x[4:])

    dmop_24h = generate_count(lambda dt: datetime(dt.year, dt.month, dt.day), '24h', dmop_df)

    dmop_24h.to_csv(os.path.join(dst_data_path + 'simple_dmop_24h' + save_postfix + '.csv'), index=True)
    print("Done.")

