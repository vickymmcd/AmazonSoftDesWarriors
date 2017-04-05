from os.path import exists
import requests
from pickle import dump, load


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
        self.file_name = file_name
        self.data_file_name = data_file_name

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
        id = self.get_id()
        url = ("https://thetracktor.com/ajax/prices/?id=" + str(id) +
               "&days=1825")
        return url

    def get_data(self):
        if exists(self.data_file_name):
            f = open(self.data_file_name, 'rb+')
            data = load(f)
        else:
            data_url = self.get_dataURL()
            f = open(self.data_file_name, 'wb+')
            data = requests.get(data_url)
            dump(data, f)
        return data

    def get_data_dict(self):
        data_file = self.get_data()
        start_key = '"prices": '
        end_key = '}}'
        data = ''
        started = False
        finished_flag = False
        for line in data_file:
            if not finished_flag:
                if start_key not in str(line) and started:
                    if end_key in str(line):
                        end_num = (str(line).index(end_key)) + len(end_key) - 1
                        data += str(line)[: end_num]
                        finished_flag = True
                    else:
                        data += str(line)
                if start_key in str(line):
                    started = True
                    start_num = str(line).index(start_key) + len(start_key)
                    if end_key in str(line):
                        end_num = (str(line).index(end_key)) + len(end_key)
                        data = str(line)[start_num: end_num]
                        finished_flag = True
                    else:
                        data += str(line)[start_num:]
        info = data.strip('{}\b')
        info = info.split('], "')
        self.data_dict = {}
        for foo in info:
            foo = foo + ']'
            foo = foo.replace('\'b\'', '')
            foo = foo.replace('\"', '')
            bar = foo.split(':')
            bar[1] = bar[1].strip()
            bar[1] = bar[1].replace('[', '')
            bar[1] = bar[1].replace(']', '')
            bar[1] = bar[1].split(',')
            bar[1][0] = float(bar[1][0])
            bar[1][1] = float(bar[1][1])
            if bar[0] not in self.data_dict:
                self.data_dict[bar[0]] = bar[1]
        return self.data_dict


collect = Collector('https://thetracktor.com/detail/B00IJJF9CI/',
                    'umbrella.txt', 'umbrella_data.txt')
collect.get_data()
