from os.path import exists
import requests
from pickle import dump, load
import ast
import json


def get_id(url, file_name):
    '''Gets the product id for the specified html file.
    Stores the html in a pickle file or acesses the file if
    it already exits.

    url: Tracktor url of website for a specific product
    file_name: file where the html is stored or should be stored
    '''
    if exists(file_name):
        f = open(file_name, 'rb+')
        page = load(f)
    else:
        f = open(file_name, 'wb+')
        page = requests.get(url)
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


def get_dataURL(url, file_name):
    id = get_id(url, file_name)
    url = "https://thetracktor.com/ajax/prices/?id=" + str(id) + "&days=360"
    return url


def get_data(url, file_name, data_file_name):
    if exists(data_file_name):
        f = open(data_file_name, 'rb+')
        data = load(f)
    else:
        data_url = get_dataURL(url, file_name)
        f = open(data_file_name, 'wb+')
        data = requests.get(data_url)
        dump(data, f)
    return data



print(get_data('https://thetracktor.com/detail/B00EPGMN1E/', 'bottle.txt', 'bottle_data.txt'))

def get_data_dict(url, file_name, data_file_name):
    data_file = get_data(url, file_name, data_file_name)
    start_key = '"prices": '
    end_key = '}}'
    data = ''
    started = False
    finished_flag = False
    for line in data_file:
        if finished_flag == False:
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
    data_dict = {}
    for foo in info:
        foo = foo + ']'
        foo = foo.replace('\'b\'','')
        foo = foo.replace('\"','')
        bar = foo.split(':')
        bar[1] = bar[1].strip()
        bar[1] = bar[1].replace('[', '')
        bar[1] = bar[1].replace(']', '')
        bar[1] = bar[1].split(',')
        bar[1][0] = float(bar[1][0])
        bar[1][1] = float(bar[1][1])
        if bar[0] not in data_dict:
            data_dict[bar[0]] = bar[1]
    return data_dict





get_data('https://thetracktor.com/detail/B00EPGMN1E/', 'bottle.txt', 'bottle_data.txt')
print(get_data_dict('https://thetracktor.com/detail/B01L8Q5NXS/', 'phone.txt','phone_data.txt'))
