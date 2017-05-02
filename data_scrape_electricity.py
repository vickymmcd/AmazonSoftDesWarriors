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
		a url, file_name, and data_file_name.

		url: url of data to obtain from Tracktor
		file_name: name of file where id of data is saved
		data_file_name: name of file where data is saved
		NOTE: Only need data_file_name and data_file if those files
		already exist, the url input can be an empty string.
		'''
		self.data_file_name = "data/" + data_file_name

	def get_data(self):
		'''
		Returns the data as read from the stored
		file.'''
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
		#print(data)
		info = data.strip("b'")
		months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
		months_epoch = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11","12"]
		for i in range(len(months)):
			#print(i)
			months_epoch[i]
			info = info.replace(months[i], months_epoch[i])
		#info = info.replace(months,months_epoch)
		#print(info)
		info = info.split("r\\n")

		#print(info)
		#info = info.replace('"id":"DCOILWTICO"' , '')
		#info = info.split('"date"')
		self.data_dict = {}
		new_dixt = {}
		for foo in info[:-1]:
			foo = foo.split(',')
			#print(foo)
			pattern = '%m %Y'
			epoch = str(time.mktime(time.strptime(foo[0],pattern)))
			self.data_dict[epoch] = [float(foo[1])]
			"""foo[1]=foo[1].strip('",')
			foo[2] = foo[2].strip('",')
			foolul = foo[2].split('"')
			pattern = '%m %Y'
			epoch = str(time.mktime(time.strptime(foo[1],pattern)))
			foolul[0]= [float(foolul[0])]
			self.data_dict[epoch] = foolul[0]"""
		return self.data_dict


#collect = Collector('',
#                    'bugspray.txt', 'more_bugspray_data.txt')
#collect.get_data_dict()
if __name__ == '__main__':
	collect = Collector("avg_elec_price")
	print(collect.get_data_dict())
