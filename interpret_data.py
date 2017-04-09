from scipy.interpolate import UnivariateSpline
from scipy.interpolate import KroghInterpolator
from format_data import Formatter
import matplotlib.pyplot as plt
import time
import numpy as np
from sklearn import svm, linear_model
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
#import seaborn as sns; sns.set()
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from sklearn.linear_model import LinearRegression


class Interpreter:
	def __init__(self, url, file_name, data_file_name, n_days):
		'''
        Initializes the data Interpreter object with
        a data Formatter object and uses that object to grab
        the formatted x and y values. Initializes the number of
        days to predict into the future and generates
        a list of wanted days.

        url: url of data to obtain from Tracktor
        file_name: name of file where id of data is saved
        data_file_name: name of file where data is saved
        NOTE: Only need data_file_name and data_file if those files
        already exist, the url input can be an empty string.
        n_days: number of days user wants the model to extrapolate
        into the future
		'''
		self.formatter = Formatter(url, file_name, data_file_name)
		self.time_series = self.formatter.data_to_dataframe()
		self.ts_log_diff = 0

	def differencing(self):
		ts_log = np.log(self.time_series)
		#print(ts_log)
		self.ts_log_diff = ts_log - ts_log.shift()
		#print(self.ts_log_diff)

	def create_acf(self):
		#min_val = np.amin(self.ts_log_diff)
		#print(self.ts_log_diff)
		#print(self.ts_log_diff.columns[])
		#print(self.ts_log_diff[[0]])
		#print(self.ts_log_diff[:0])
		np_to_list= []
		for i in self.ts_log_diff.iloc[:, 0].tolist():
			np_to_list.append(i)

		x_values =[]
		min_val = min(np_to_list[1:])
		print(min_val)
		for x in np_to_list:
			#print(x)
			x = x - min_val
			x_values.append(x)
			print(x)
		print(np_to_list)
		print(x_values)
		lag_acf = acf(x_values[1:],nlags=15)
		#print(lag_acf)
		lag_pacf = pacf(x_values[1:],nlags=20, method = 'ols')
		#print(lag_pacf)
		"""plt.figure()
		plt.subplot(lag_acf, 'ro')
		plt.show()"""
		#for a 95% confidence interval
		#Plot ACF:
		plt.subplot(121)
		plt.plot(lag_acf)
		plt.axhline(y=0,linestyle='--',color='gray')
		plt.axhline(y=-1.96/np.sqrt(len(x_values)),linestyle='--',color='gray')
		plt.axhline(y=1.96/np.sqrt(len(x_values)),linestyle='--',color='gray')
		plt.title('Autocorrelation Function')

		plt.subplot(122)
		plt.plot(lag_pacf)
		plt.axhline(y=0,linestyle='--',color='gray')
		plt.axhline(y=-1.96/np.sqrt(len(x_values)),linestyle='--',color='gray')
		plt.axhline(y=1.96/np.sqrt(len(x_values)),linestyle='--',color='gray')
		plt.title('Partial Autocorrelation Function')
		plt.tight_layout()
		plt.show()








#test_interpreter = Interpreter('', 'camera.txt', 'camera_data.txt',30)
myinterpreter = Interpreter('', 'phone.txt', 'phone_data.txt', 30)
myinterpreter.differencing()
myinterpreter.create_acf()
