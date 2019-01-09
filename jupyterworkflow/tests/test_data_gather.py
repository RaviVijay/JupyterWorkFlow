from jupyterworkflow.data_gather import get_fremont_data,get_data
import pandas as pd
import numpy as np

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index,pd.DatetimeIndex)
    assert len(np.unique(data.index.time))==24

