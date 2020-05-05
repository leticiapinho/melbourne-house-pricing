import pandas as pd

from functions import *


class Houses:
    def __init__(self):
        _data = pd.read_csv('data_raw_Melbourne_housing_FULL.csv')
        self.data = pd.DataFrame(_data)

        self.preProcessData()

    def preProcessData(self):
        data = self.data
        data['Date'] = pd.to_datetime(data['Date'])

        data['Age'] = 2020 - data['YearBuilt']

    # Remove outliers
        data = data[(data['Age'] < 185)]

        self.dataProcessado = self.data.copy()

    def getHead(self):
        pd.set_option('display.max_columns', None)
        return self.data
