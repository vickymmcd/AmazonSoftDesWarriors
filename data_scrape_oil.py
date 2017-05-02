from os.path import exists
from pickle import dump, load
import requests
import csv
import time

class Collector:
	def __init__(self, data_file_name):
		'''
		Initializes the data Collector object with
		a url, file_name, and data_file_name.

		url: url of data to obtain from Tracktor
		file_name: name of file where id of data is saved
		data_file_name: name of file where data is saved
		NOTE: Only need data_file_name and data_file if those files
		already exist, the url input can be an empty string.
		'''
		self.data_file_name = 'data/' + data_file_name

	def get_data(self):
		'''
		Returns the data as read from the stored
		file.'''
		f = open(self.data_file_name, 'rb+')
		data = f.read()
		return data

	def get_data_dict(self):
		'''
		Returns a dictionary of the data for the
		given product.
		'''
		data_file = self.get_data()
		data = str(data_file)
		info = data.strip('b[{}')
		info = info.replace('"id":"DCOILWTICO"' , '')
		info = info.split('"date"')
		self.data_dict = {}
		new_dixt = {}
		for foo in info[400:]:
			foo = foo.strip('""')
			foo = foo.replace("close","")
			foo = foo.split(':')
			foo[1]=foo[1].strip('",')
			foo[2] = foo[2].strip('",')
			foolul = foo[2].split('"')
			pattern = '%Y-%m-%d'
			epoch = str(time.mktime(time.strptime(foo[1],pattern)))
			foolul[0]= [float(foolul[0])]
			self.data_dict[epoch] = foolul[0]
		return self.data_dict


#collect = Collector('',
#                    'bugspray.txt', 'more_bugspray_data.txt')
#collect.get_data_dict()
if __name__ == '__main__':
	collect = Collector("oil_prices")
	collect.get_data_dict()
