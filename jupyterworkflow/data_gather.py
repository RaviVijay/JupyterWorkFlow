import pandas as pd
from pathlib import Path
import requests

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename = 'Fremont.csv', url = FREMONT_URL, force_download=True):
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
    data = get_data(filename, url, force_download, 'Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    
    data.columns = ['West', 'East']
    data['Total'] = data['East']+ data['West']
    return data


def get_data(filename, url, force_download=True, index_col=""):
    """ Download  data and return Dataframe
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
    filename = Path(filename)
    if force_download or not filename.exists():
        content = requests.get(url).content
        filename.open('wb').write(content)

    if index_col == "":
        data = pd.read_csv(filename)
    else:
        data = pd.read_csv(filename,index_col = index_col)
    return data