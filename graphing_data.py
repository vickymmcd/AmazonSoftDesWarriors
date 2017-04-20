from format_data import Formatter
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import math

class Grapher:
	'''
	contains functions and classes to graph time series
	'''
	def __init__(self, url, file_name, data_file_name):
		self.ts_data = Formatter(url, file_name, data_file_name)
		self.ts_frame = self.ts_data.data_to_dataframe()

	def decompose_ts(self):
		self.ts_decomposition = seasonal_decompose(self.ts_frame, freq=365)
		self.seasonal = self.ts_decomposition.seasonal.dropna()
		self.trend = self.ts_decomposition.trend.dropna()
		self.resid = self.ts_decomposition.resid
		resid_list = []
		for i in self.resid.iloc[:, 0].tolist():
			resid_list.append(i)
		print(resid_list)
		for i in range(len(resid_list)):
			if math.isnan(resid_list[i]) != True:
				start_i = i
				break
		print(start_i)
		resid_list1= resid_list[start_i:]
		for i in range(len(resid_list1)):
			if math.isnan(resid_list1[i]) == True:
				end_i = i
				break
		print(end_i)
		#print(resid_list[start_i:end_i])
		self.resid= self.resid.dropna()
		#print(self.resid)
		return self.resid, start_i, end_i

	def get_data(self):
		return self.ts_frame


# from bokeh.charts import Line, show, output_file
mygrapher = Grapher("", "christmas.txt", "christmas_data.txt")
mygrapher.decompose_ts()
plt.figure()
plt.plot(mygrapher.ts_frame)
plt.plot(mygrapher.trend)
plt.plot(mygrapher.seasonal)
plt.plot(mygrapher.resid)
#plt.show()
