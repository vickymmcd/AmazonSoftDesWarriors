from os.path import exists
from pickle import dump, load
import requests
import csv
import time

class Collector:
	def __init__(self, data_file_name):
		'''
		Initializes the data Collector object with
		a data_file_name.

		data_file_name: name of file where data is saved
		'''
		self.data_file_name = 'data/' + data_file_name

	def get_data(self):
		'''
		Returns the data as read from the stored
		file.
		'''
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
<<<<<<< HEAD
		for foo in info[600:]:
=======
		for foo in info[700:]:
>>>>>>> 6d188b232f0cdbe5cbf497563b86a000f8d4e3db
			foo = foo.strip('""')
			foo = foo.replace("close","")
			foo = foo.split(':')
			foo[1]=foo[1].strip('",')
			foo[2] = foo[2].strip('",')
			final_foo = foo[2].split('"')
			pattern = '%Y-%m-%d'
			epoch = str(time.mktime(time.strptime(foo[1],pattern)))
<<<<<<< HEAD
			final_foo[0]= [float(final_foo[0])]
			self.data_dict[epoch] = final_foo[0]
			print(len(self.data_dict))
=======
			foolul[0]= [float(foolul[0])]
			self.data_dict[epoch] = foolul[0]
>>>>>>> 6d188b232f0cdbe5cbf497563b86a000f8d4e3db
		return self.data_dict


if __name__ == '__main__':
	collect = Collector("oil_prices")
	collect.get_data_dict()
