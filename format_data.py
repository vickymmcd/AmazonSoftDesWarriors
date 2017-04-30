'''
helper functions for super shoppers final product for softdes spring 2017
formats dates and times, and prepares data for machine learning process
'''
import time
import datetime
import pandas as pd
from data_scrape_electricity import Collector
import numpy as np


class Formatter:
    def __init__(self, url, file_name, data_file_name):
        '''
        Initializes the data Formatter object with
        a dictionary of data to be formatted.

        url: url of data to obtain from Tracktor
        file_name: name of file where id of data is saved
        data_file_name: name of file where data is saved
        NOTE: Only need data_file_name and data_file if they
        already exist, the other input can be an empty string.
        '''
        self.collector = Collector(data_file_name)
        self.data_dict = self.collector.get_data_dict()
        self.x_values = []
        self.y_values = []
        self.dict = {}
        #self.add_in_between_dates()

    def add_in_between_dates(self):
        keys = [float(key) for key in self.data_dict]
        keys.sort()
        for i, key in enumerate(keys):
            temp = key
            if i < len(keys) - 1:
                while(self.add_day(temp) < keys[i+1]):
                    self.data_dict[str(self.add_day(temp))] = self.data_dict[str(key)]
                    temp = self.add_day(temp)

    def get_date(self, epoch_time):
        t = time.gmtime(epoch_time)
        return t

    def add_day(self, epoch_time):
        t = ((epoch_time/1000) + (3600 * 24)) * 1000
        return t

    def data_to_matrix(self):
        self.x_values = [float(key)/1000 for key in self.data_dict.keys()]
        #self.x_values = [float(key) for key in self.data_dict.keys()]
        self.y_values = [float(val[0]) for val in self.data_dict.values()]
        return self.x_values, self.y_values

    def get_formatted_dict(self):
        data = pd.DataFrame(self.data_dict)
        return self.data_dict

    def data_to_dataframe(self):
        formatted_dict = {}
        print(len(self.data_dict))
        for key in self.data_dict:
            new_key = datetime.datetime.fromtimestamp(float(key)).strftime('%Y-%m-%d')
            new_key_date = datetime.datetime.fromtimestamp(float(key))
            #print(new_key_date.month)
            if new_key not in formatted_dict:
                formatted_dict[new_key] = self.data_dict[key]
        print(formatted_dict)
        frame = pd.DataFrame(formatted_dict).T
        print(frame)
        frame.index = np.array(frame.index)
        frame.index= np.array(frame.index, dtype='datetime64[us]')
        frame.index.astype('datetime64[ns]')
        #print(frame)
        return frame


if __name__ == '__main__':
	myformat = Formatter('', '', 'avg_elec_price')
	data = myformat.data_to_dataframe()
	print(data)
