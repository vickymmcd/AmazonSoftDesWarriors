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


def get_data_dict(url, file_name, data_file_name):
    data_file = get_data(url, file_name, data_file_name)
    start_key = '"prices": '
    end_key = '}}'
    data = ''
    started = False
    for line in data_file:
        if start_key not in str(line) and started:
            if end_key in str(line):
                end_num = (str(line).index(end_key)) + len(end_key) - 1
                data += str(line)[: end_num]
                return data
            else:
                data += str(line)
        if start_key in str(line):
            started = True
            start_num = str(line).index(start_key) + len(start_key)
            if end_key in str(line):
                end_num = (str(line).index(end_key)) + len(end_key)
                data = str(line)[start_num: end_num]
                return data
            else:
                data += str(line)[start_num:]


# get_data('https://thetracktor.com/detail/B01L8Q5NXS/', 'camera.txt',
#          'camera_data.txt')
info = get_data_dict('https://thetracktor.com/detail/B01L8Q5NXS/', 'phone.txt',
         'phone_data.txt')

info
info = info.strip('{}\b')
info = info.split('], "')
info

price_dict = {}
for foo in info:
    foo = foo + ']'
    foo = foo.strip('\\b"')
    # foo = foo.split(':')
    # foo[1] = foo[1].strip('"')
    print(foo)
    print('\n\n')
'''mydict = get_data_dict('', 'phone.txt', 'phone_data.txt')
json_string = json.dumps(mydict)
mynewdict = json.loads(mydict)
x = mynewdict["1459677512000.0"]
# print((get_data_dict('', 'phone.txt', 'phone_data.txt')))
print(x)
# print(mydict["1459677512000.0"])'''
