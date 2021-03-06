'''
helper functions for super shoppers final product for softdes spring 2017
formats dates and times, and prepares data for machine learning process
'''
from os.path import exists
from pickle import dump, load
import time
import datetime
import pandas as pd
from data_scrape_electricity import Collector as Collector_elec
from data_scrape_oil import Collector as Collector_oil
import numpy as np


class Formatter:
    def __init__(self, data_file_name):
        '''
        Initializes the data Formatter object with
        a dictionary of data to be formatted.

        data_file_name: name of file where data is saved
        '''
        self.formatted_data_file = 'data/'+data_file_name + '_formatted.txt'
        self.frame = None
        if data_file_name == 'avg_elec_price':
            if exists(self.formatted_data_file):
                self.frame = pd.read_pickle(self.formatted_data_file)
            else:
                self.collector = Collector_elec(data_file_name)
                self.data_dict = self.collector.get_data_dict()
        if data_file_name == 'oil_prices':
            if exists(self.formatted_data_file):
                self.frame = pd.read_pickle(self.formatted_data_file)
            else:
                self.collector = Collector_oil(data_file_name)
                self.data_dict = self.collector.get_data_dict()
        self.x_values = []
        self.y_values = []
        self.dict = {}

    def add_in_between_dates(self):
        '''
        Adds dates in between given data so that we have
        data points for each individual day.
        '''
        keys = [float(key) for key in self.data_dict]
        keys.sort()
        for i, key in enumerate(keys):
            temp = key
            if i < len(keys) - 1:
                while(self.add_day(temp) < keys[i+1]):
                    self.data_dict[str(self.add_day(temp))] = self.data_dict[str(key)]
                    temp = self.add_day(temp)

    def get_date(self, epoch_time):
        '''
        Gets the date associated with the given epoch time

        epoch_time: epoch you want as a datetime
        '''
        t = time.gmtime(epoch_time)
        return t

    def add_day(self, epoch_time):
        '''
        Adds a day to the given epoch_time

        epoch_time: epoch you want with an additional day
        returns: epoch with 1 day added
        '''
        t = ((epoch_time/1000) + (3600 * 24)) * 1000
        return t

    def get_formatted_dict(self):
        '''
        Returns the formatted data dictionary
        '''
        data = pd.DataFrame(self.data_dict)
        return self.data_dict

    def data_to_dataframe(self):
        '''
        Converts the data dictionary into a pandas DataFrame
        and returns that dataframe.
        '''
        if exists(self.formatted_data_file):
            return self.frame
        formatted_dict = {}
        for key in self.data_dict:
            new_key = datetime.datetime.fromtimestamp(float(key)).strftime('%Y-%m-%d')
            new_key_date = datetime.datetime.fromtimestamp(float(key))
        for key in self.data_dict:
            new_key = datetime.datetime.fromtimestamp(float(key)).strftime('%Y-%m-%d')
            new_key_date = datetime.datetime.fromtimestamp(float(key))
            if new_key not in formatted_dict:
                formatted_dict[new_key] = self.data_dict[key]
        frame = pd.DataFrame(formatted_dict).T

        frame.index = np.array(frame.index)
        frame.index = np.array(frame.index, dtype = 'datetime64[us]')
        frame.index.astype('datetime64[ns]')
        frame.to_pickle(self.formatted_data_file)
        return frame


if __name__ == '__main__':
	myformat = Formatter('oil_prices')
	data = myformat.data_to_dataframe()
