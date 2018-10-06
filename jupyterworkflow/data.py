from urllib.request import urlretrieve
import pandas as pd
import os

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=True):
    """ Download and cache the fremont data
    Parameters
    -----
    filename : string (optional)
        location to save the data
    url: string(optional)
        web location of the data
    force_download: bool (optional)
        if True, force download
    
    Returns
    -----
    data: pandas.DF
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(FREMONT_URL, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv',index_col='Date',parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['East']+ data['West']
    return data