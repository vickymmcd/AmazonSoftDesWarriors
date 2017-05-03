from os.path import exists
from pickle import dump, load
import requests
import csv
import time
import pandas as pd

class Collector:
	def __init__(self, data_file_name):
		'''
		Initializes the data Collector object with
		a data_file_name.

		data_file_name: name of file where data is saved
		'''
		self.data_file_name = "data/" + data_file_name

	def get_data(self):
		'''
		Returns the data as read from the stored
		file.
		'''
		f= open(self.data_file_name, 'rb+')
		data = f.read()
		#print(data)
		return data

	def get_data_dict(self):
		'''
		Returns a dictionary of the data for the
		given product.
		'''
		data_file = self.get_data()
		data = str(data_file)
		info = data.strip("b'")
		months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
		months_epoch = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11","12"]
		for i in range(len(months)):
			months_epoch[i]
			info = info.replace(months[i], months_epoch[i])
		info = info.split("r\\n")
		self.data_dict = {}
		new_dixt = {}
		for foo in info[:-1]:
			foo = foo.split(',')
			#print(foo)
			pattern = '%m %Y'
			epoch = str(time.mktime(time.strptime(foo[0],pattern)))
			self.data_dict[epoch] = [float(foo[1])]
		return self.data_dict


#collect = Collector('',
#                    'bugspray.txt', 'more_bugspray_data.txt')
#collect.get_data_dict()
if __name__ == '__main__':
	collect = Collector("avg_elec_price")
	print(collect.get_data_dict())
