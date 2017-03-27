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


get_id('https://thetracktor.com/detail/B00GJWJI88/', 'bugspray.txt')
