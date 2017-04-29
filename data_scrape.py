from os.path import exists
from pickle import dump, load
import requests
import csv

class Collector:
    def __init__(self, url, file_name, data_file_name):
        '''
        Initializes the data Collector object with
        a url, file_name, and data_file_name.

        url: url of data to obtain from Tracktor
        file_name: name of file where id of data is saved
        data_file_name: name of file where data is saved
        NOTE: Only need data_file_name and data_file if those files
        already exist, the url input can be an empty string.
        '''
        self.url = url
        self.file_name = 'data/' + file_name
        self.data_file_name = 'data/' + data_file_name

    def get_id(self):
        '''Gets the product id for the specified html file.
        Stores the html in a pickle file or acesses the file if
        it already exits.
        '''
        if exists(self.file_name):
            f = open(self.file_name, 'rb+')
            page = load(f)
        else:
            f = open(self.file_name, 'wb+')
            page = requests.get(self.url)
            dump(page, f)

        key = 'Tracktor.loadPrices'
        for line in page:
            if key in str(line):
                myLine = str(line)
                num = myLine.index(key)
                num += len(key) + 1
                endnum = num + myLine[num:].index(',')
                print(myLine[num:endnum])
                return myLine[num:endnum]

    def get_dataURL(self):
        '''
        Gets the url that is associated with the product's
        data based on its id.
        '''
        id = self.get_id()
        url = ("https://thetracktor.com/ajax/prices/?id=" + str(id).strip() +
               "&days=1825")
        return url

    def get_data(self):
        '''
        Returns the data as read from the stored
        file.
        '''
        if exists(self.data_file_name):
            f = open(self.data_file_name, 'rb+')
            data = f.read()
        else:
            data_url = self.get_dataURL()
            data = requests.get(data_url)
            f = open(self.data_file_name, 'wb+')
            dump(data, f)
            '''
            with open(self.data_file_name, "w", encoding='UTF-8') as w:
                writer = csv.writer(w)
                writer.writerow([str(d, 'UTF-8') for d in data])'''
        return data

    def get_data_dict(self):
        '''
        Returns a dictionary of the data for the
        given product.
        '''
        data_file = self.get_data()
        data = str(data_file)
        info = data.strip('b\'{}}\n')
        info = info.split('], "')
        self.data_dict = {}
        for foo in info:
            foo = foo + ']'
            foo = foo.replace('\'b\'', '')
            foo = foo.replace('\"', '')
            bar = foo.split(':')
            try:
                bar[1] = bar[1].strip()
            except:
                print(bar)
            bar[1] = bar[1].replace('[', '')
            bar[1] = bar[1].replace(']', '')
            bar[1] = bar[1].split(',')
            while len(bar[1][0]) > 0 and not bar[1][0].replace('.','',1).isdigit():
                bar[1][0] = bar[1][0][:-1]
            if bar[1][0] == '': bar[1][0] = 0
            else: bar[1][0] = float(bar[1][0])
            if len(bar[1]) > 1:
                bar[1][1] = bar[1][1].strip()
                while len(bar[1][1]) > 0 and not bar[1][1].replace('.','',1).isdigit():
                    bar[1][1] = bar[1][1][:-1]
                if bar[1][1] == '':
                    bar[1][1] = 0
                else:
                    bar[1][1] = float(bar[1][1])
            if bar[0] not in self.data_dict:
                self.data_dict[bar[0]] = [bar[1][0]]
        return self.data_dict




#collect = Collector('',
#                    'bugspray.txt', 'more_bugspray_data.txt')
#collect.get_data_dict()

if __name__ == '__main__':
    collect = Collector('', 'gloves.txt', 'more_gloves_data.txt')
    collect.get_data_dict()
