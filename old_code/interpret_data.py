from scipy.interpolate import UnivariateSpline
from scipy.interpolate import KroghInterpolator
from format_data import Formatter
import matplotlib.pyplot as plt
import time
import numpy as np
from graphing_data import Grapher
from sklearn import svm, linear_model
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd



class Interpreter:
	def __init__(self, url, file_name, data_file_name, n_days):
		'''
		Initializes the data Interpreter object with
		a data Formatter object and uses that object to grab
		the formatted x and y values. Initializes the number of
		days to predict into the future and generates
		a list of wanted days.
		'''
		self.formatter = Formatter(url, file_name, data_file_name)
		self.time_series = self.formatter.data_to_dataframe()
		self.ts_log_diff = 0
		self.ts_log = 0
		self.graphing = Grapher(url,file_name,data_file_name)
		self.resid, self.seasonal, self.trend, self.start_i,self.end_i = self.graphing.decompose_ts()

	def differencing(self):
		'''
		Does the differencing for the time series and its shift
		'''
		self.ts_log = np.log(self.time_series)
		self.ts_log_diff = self.ts_log - self.ts_log.shift()

	def create_acf(self):
		'''
		Creates acf and pacf plots for the time series data
		'''
		np_to_list= []
		for i in self.ts_log_diff.iloc[:, 0].tolist():
			np_to_list.append(i)

		self.prices =[]
		min_val = min(np_to_list[1:])
		for x in np_to_list:
			x = x - min_val
			self.prices.append(x)
		self.lag_acf = acf(self.prices[1:],nlags=20)
		self.lag_pacf = pacf(self.prices[1:],nlags=20, method = 'ols')
		#for a 95% confidence interval
		#Plot ACF:
		"""plt.subplot(121)
		plt.plot(self.lag_acf)
		plt.axhline(y=0,linestyle='--',color='gray')
		plt.axhline(y=-1.65/np.sqrt(len(self.prices)),linestyle='--',color='gray')
		plt.axhline(y=1.65/np.sqrt(len(self.prices)),linestyle='--',color='gray')
		plt.title('Autocorrelation Function')"""

	def do_ARIMA(self):
		'''
		Sets up and graphs the ARIMA forecasting for the time series
		Continous error at line 102:  ufunc 'add' did not contain a loop with signature matching types dtype('<U21') dtype('<U21') dtype('<U21')
		We are trying to use the stationary time series as an input to our model, but neither the stationary
		nor the original work.
		'''
		# Find intersection with the top line for each graph
		threshold = .03
		top_y = 1.65/np.sqrt(len(self.prices))
		for i, val in enumerate(self.lag_acf):
		    if val < top_y + threshold:
		        q = i
		        break
		for i, val in enumerate(self.lag_pacf):
		    if val < top_y + threshold:
		        p = i
		        break
		print('the p')
		print(p)
		print('the q')
		print(q)
		#print(self.resid)
		#determining whether or not we use the stationary time series data: why is it not working?
		resid_list = []
		#print(self.resid)
		for i in self.resid.iloc[:, 0].tolist():
			resid_list.append(i)

		model = ARIMA(resid_list, order=(p, 1, q))
		results_ARIMA = model.fit(disp=-1)
		print(len(resid_list))
		print(resid_list)
		#arima.predict(start='2017-01-11', end='2017-01-12')
		prediction = results_ARIMA.predict(start= 1464, end=1466)
		plt.subplot(122)
		plt.plot(resid_list)
		plt.show()
		print(prediction)
		print(self.seasonal[self.start_i:self.end_i])
		print(self.trend[self.start_i:self.end_i])

		return prediction



if __name__ == '__main__':
	myinterpreter = Interpreter('', '', 'oil_prices', 30)
	myinterpreter.differencing()
	myinterpreter.create_acf()
	myinterpreter.do_ARIMA()
