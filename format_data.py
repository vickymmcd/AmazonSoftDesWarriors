
from scipy.interpolate import KroghInterpolator

def data_to_matrix():
    self.x_values = [key for key in self.data_dict.keys()]
    self.y_values =[val[0] for val in self.data_dict.values()]
    return self.x_values , self.y_values

dict1= {1:[2,3], 3:[4,5]}
data_to_function(dict1)

'''
helper functions for super shoppers final product for softdes spring 2017
formats dates and times, and prepares data for machine learning process
'''

import time
from data_scrape import get_data_dict


class Formatter:
    def __init__(self, url, file_name, data_file_name):
        '''
        Initializes the data Formatter object with
        a dictionary of data to be formatted.

        url: url of data to obtain from Tracktor
        file_name: name of file where id of data is saved
        data_file_name: name of file where data is saved
        NOTE: Only need data_file_name if it already exists
        other two inputs can be empty strings
        '''
        self.data_dict = get_data_dict(url, file_name, data_file_name)

    def add_in_between_dates(self):
        self.data_dict

    def get_date(self, epoch_time):
        t = time.gmtime(epoch_time)
        return t

    def add_day(self, epoch_time):
        t = epoch_time + (3600 * 24)
        return t
