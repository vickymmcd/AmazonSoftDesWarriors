from os.path import exists
import requests
from pickle import dump, load


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
    print(data)


print(get_data('', 'camera.txt', 'camera_data.txt'))
