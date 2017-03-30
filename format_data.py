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
        NOTE: Only need data_file_name and data_file if they
        already exist, the other input can be an empty string.
        '''
        self.data_dict = get_data_dict(url, file_name, data_file_name)
        self.x_values = []
        self.y_values = []

    def add_in_between_dates(self):
        keys = [float(key) for key in self.data_dict]
        keys.sort()
        for i, key in enumerate(keys):
            temp = key
            if i < len(keys) - 1:
                while(self.add_day(temp) < keys[i+1]):
                    self.data_dict[str(self.add_day(key))] = self.data_dict[str(key)]
                    temp = self.add_day(temp)

    def get_date(self, epoch_time):
        t = time.gmtime(epoch_time)
        return t

    def add_day(self, epoch_time):
        t = epoch_time + (3600 * 24)
        return t

    def get_formatted_dict(self):
        self.add_in_between_dates()
        return self.data_dict


test_formatter = Formatter('', 'camera.txt', 'camera_data.txt')
print(test_formatter.get_formatted_dict())
