from os.path import exists
import requests
import csv

class Collector:
    def __init__(self, data_file_name):
        '''
        Initializes the data Collector object with
        a data_file_name.

        data_file_name: name of file to read in data from
        '''
        self.data_file_name = data_file_name
        self.data = ''

    def get_data(self):
        '''
        '''
        if exists(self.data_file_name):
            f = open(self.data_file_name, 'rb+')
            self.data = f.read()
        return self.data

    def get_data_dict(self):
        '''
        '''
        self.data = str(self.data).split('},{')
        self.data = [item.strip('"id":"DCOILWTICO","date":"') for item in self.data]
        self.data = [item[:item.index('close1')] for item in self.data]
        print(self.data[0].strip('b'[{"id":"DCOILWTICO","date":"'))



if __name__ == '__main__':
    collect = Collector('oil_prices')
    collect.get_data()
    collect.get_data_dict()
