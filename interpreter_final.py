
from format_data import Formatter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from graphing_data import Grapher
import pandas as pd
from statsmodels.tsa.stattools import adfuller, acf, pacf
import statsmodels.api as sm
import datetime
from dateutil.relativedelta import relativedelta




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
		self.time_series.columns=['Price']
		self.season = 12
		self.days= n_days + self.days_between()
		self.months= self.days /30
		self.Q =0
		self.P =0
		self.p=0
		self.q=0

	def days_between(self):
		dt = datetime.datetime.now()
		d2= self.time_series.index[-1]
		return abs((dt-d2).days)

	def differencing(self):
		'''
		Does the differencing for the time series and its shift
		'''
		self.time_series["first_difference"] = self.time_series['Price'] - self.time_series['Price'].shift(1)
		self.time_series["seasonal_difference"] = self.time_series['Price'] - self.time_series['Price'].shift(self.season)
		self.time_series["seasonal_first_difference"]= self.time_series["first_difference"]- self.time_series["first_difference"].shift(self.season)
		# self.test_stationarity(self.time_series["first_difference"].dropna(inplace=False))
		# self.test_stationarity(self.time_series["seasonal_difference"].dropna(inplace=False))
		# self.test_stationarity(self.time_series["seasonal_first_difference"].dropna(inplace=False))


	def test_stationarity(self,timeseries):

		#Determing rolling statistics
		rolmean = timeseries.rolling(window = 12).mean()
		rolstd = timeseries.rolling(window = 12).std()

		#Plot rolling statistics:
		fig = plt.figure(figsize=(12, 8))
		orig = plt.plot(timeseries, color='blue',label='Original')
		mean = plt.plot(rolmean, color='red', label='Rolling Mean')
		std = plt.plot(rolstd, color='black', label = 'Rolling Std')
		plt.legend(loc='best')
		plt.title('Rolling Mean & Standard Deviation')
		#Perform Dickey-Fuller test:
		#print('Results of Dickey-Fuller Test:')
		#print(timeseries.dropna())
		dftest = adfuller(timeseries.dropna(), autolag='AIC')
		dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
		for key,value in dftest[4].items():
		    dfoutput['Critical Value (%s)'%key] = value
		#print(dfoutput)

	def create_acf(self):
		'''
		Creates acf and pacf plots for the time series data
		'''
		#print(self.time_series)
		#print(self.time_series.iloc[2: ])
		"""
		self.prices =[]
		min_val = min(np_to_list[1:])
		for x in np_to_list:
			x = x - min_val
			self.prices.append(x)"""
		self.lag_acf = acf(self.time_series["seasonal_first_difference"].iloc[self.season+1:],nlags=20)
		self.lag_pacf = pacf(self.time_series["seasonal_first_difference"].iloc[self.season+1:],nlags=20, method = 'ols')
		self.lag_acf_1 = acf(self.time_series["first_difference"].iloc[self.season+1:],nlags=20)
		self.lag_pacf_1 = pacf(self.time_series["first_difference"].iloc[self.season+1:],nlags=20, method = 'ols')
		#for a 95% confidence interval
		#Plot ACF:

	def get_p_and_q(self):
		'''
		Sets up and graphs the ARIMA forecasting for the time series
		Continous error at line 102:  ufunc 'add' did not contain a loop with signature matching types dtype('<U21') dtype('<U21') dtype('<U21')
		We are trying to use the stationary time series as an input to our model, but neither the stationary
		nor the original work.
		'''
		# Find intersection with the top line for each graph
		threshold = .03
		self.start = len(self.time_series)
		top_y = 1.65/np.sqrt(len(self.time_series["seasonal_first_difference"]))
		for i, val in enumerate(self.lag_acf):
		    if val < top_y + threshold:
		        self.Q = i
		        break
		for i, val in enumerate(self.lag_pacf):
		    if val < top_y + threshold:
		        self.P = i
		        break
		#print('the P')
		#print(self.P)
		#print('the Q')
		#print(self.Q)
		top_y = 1.65/np.sqrt(len(self.time_series["first_difference"]))
		for i, val in enumerate(self.lag_acf_1):
		    if val < top_y + threshold:
		        self.q = i
		        break
		for i, val in enumerate(self.lag_pacf_1):
		    if val < top_y + threshold:
		        self.p = i
		        break
		#print('the p')
		#print(self.p)
		#print('the q')
		#print(self.q)

	def build_model(self):
		model = sm.tsa.statespace.SARIMAX(self.time_series['Price'], trend='n', order=(self.p,1,self.q), seasonal_order=(self.P,1,self.Q,self.season), enforce_stationarity= False, enforce_invertibility=False)
		self.results= model.fit()
		#print('cat')
		#print(self.results.summary())
		#print(self.results)
		#print(self.time_series)

		#start = datetime.datetime.strptime(self.time_series.index[-1], "%Y-%m-%d")
		start = self.time_series.index[-1]
		date_list = [start + relativedelta(months=x) for x in range(0,int(self.months))]
		future = pd.DataFrame(index=date_list, columns= self.time_series.columns)
		self.time_series = pd.concat([self.time_series, future])
		self.time_series["Predictions"] = self.results.predict(start = self.start, end= 2000, dynamic = True)


	def get_data_source(self):
		return self.time_series


if __name__ == '__main__':
	myinterpreter = Interpreter('', '', 'avg_elec_price', 30)
	myinterpreter.differencing()
	#myinterpreter.test_stationarity()
	myinterpreter.create_acf()
	myinterpreter.get_p_and_q()
	myinterpreter.build_model()
	#myinterpreter.make_predictions()
