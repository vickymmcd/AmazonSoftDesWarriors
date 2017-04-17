from format_data import Formatter
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


class Grapher:
	'''
	contains functions and classes to graph time series
	'''
	def __init__(self, url, file_name, data_file_name):
		self.ts_data = Formatter(url, file_name, data_file_name)
		self.ts_frame = self.ts_data.data_to_dataframe()

	def decompose_ts(self):
		self.ts_decomposition = seasonal_decompose(self.ts_frame, freq=365)
		self.seasonal = self.ts_decomposition.seasonal#.dropna()
		self.trend = self.ts_decomposition.trend#.dropna()
		self.resid = self.ts_decomposition.resid.dropna()
		return self.seasonal, self.trend, self.resid

	def get_data(self):
		return self.ts_frame


# from bokeh.charts import Line, show, output_file
mygrapher = Grapher("", "christmas.txt", "christmas_data.txt")
mygrapher.decompose_ts()
"""
plt.figure()
plt.plot(mygrapher.ts_frame)
plt.plot(mygrapher.trend)
plt.plot(mygrapher.seasonal)
plt.plot(mygrapher.resid)
plt.show()
"""
