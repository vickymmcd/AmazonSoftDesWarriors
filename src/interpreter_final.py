
from format_data import Formatter
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, acf, pacf
import statsmodels.api as sm
import datetime
from dateutil.relativedelta import relativedelta


class Interpreter:
	def __init__(self, data_file_name, n_days):
		'''
		Initializes the data Interpreter object with
		a data Formatter object and uses that object to grab
		the formatted x and y values. Initializes the number of
		days to predict into the future and generates
		a list of wanted days.
		'''
		self.formatter = Formatter(data_file_name)
		self.time_series = self.formatter.data_to_dataframe()
		self.time_series.columns = ['Price']
		self.season = 12
		self.days = n_days + self.days_between()
		self.months = self.days /30
		self.lag_acf,self.lag_pacf, self.lag_acf_1,self.lag_pacf_1 = self.create_acf()
		self.p, self.q, self.P, self.Q = self.get_p_and_q()

	def days_between(self):
		dt = datetime.datetime.now()
		d2 = self.time_series.index[-1]
		return abs((dt-d2).days)

	def differencing(self):
		'''
		Does the differencing for the time series and for the seasonality
		'''
		self.time_series['first_difference'] = self.time_series['Price'] - self.time_series['Price'].shift(1)
		self.time_series['seasonal_difference'] = self.time_series['Price'] - self.time_series['Price'].shift(self.season)
		self.time_series['seasonal_first_difference'] = self.time_series['first_difference']- self.time_series['first_difference'].shift(self.season)
		return self.time_series['first_difference'], self.time_series['seasonal_difference'], self.time_series['seasonal_first_difference']


	def test_stationarity(self,timeseries):
		'''
		Determines whether the data is stationary through the Dickey-Fuller test. The lower the p-value, the more stationary the data.
		'''
		#Determing rolling statistics
		rolmean = timeseries.rolling(window = 12).mean()
		rolstd = timeseries.rolling(window = 12).std()

		#Perform Dickey-Fuller test:
		dftest = adfuller(timeseries.dropna(), autolag='AIC')
		dfoutput = pd.Series(dftest[0:4], index = ['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
		for key,value in dftest[4].items():
			dfoutput['Critical Value (%s)'%key] = value

	def create_acf(self):
		'''
		Finds the autocorrelation and partial autocorrelation functions of the seasonal first difference and of the differenced data
		'''
		self.time_series['first_difference'], self.time_series['seasonal_difference'], self.time_series['seasonal_first_difference'] = self.differencing()
		self.lag_acf = acf(self.time_series['seasonal_first_difference'].iloc[self.season+1:],nlags = 20)
		self.lag_pacf = pacf(self.time_series['seasonal_first_difference'].iloc[self.season+1:],nlags = 20, method = 'ols')
		self.lag_acf_1 = acf(self.time_series['first_difference'].iloc[self.season+1:],nlags = 20)
		self.lag_pacf_1 = pacf(self.time_series['first_difference'].iloc[self.season+1:],nlags = 20, method = 'ols')
		return self.lag_acf,self.lag_pacf, self.lag_acf_1,self.lag_pacf_1


	def get_p_and_q(self):
		'''
		Finds the parameters of the model for the stationary and the first difference (p and q values) by finding the intersection of the second standard deviation away and the data series.
		'''
		# Find intersection with the top line for each graph
		threshold = .03
		# Find the p and q values for the differenced seasonality
		self.start = len(self.time_series)
		top_y = 1.65/np.sqrt(len(self.time_series['seasonal_first_difference']))
		for i, val in enumerate(self.lag_acf):
			if val < top_y + threshold:
				self.Q = i
				break
		for i, val in enumerate(self.lag_pacf):
			if val < top_y + threshold:
				self.P = i
				break

		# Find the p and q values for the differenced data series
		top_y = 1.65/np.sqrt(len(self.time_series['first_difference']))
		for i, val in enumerate(self.lag_acf_1):
			if val < top_y + threshold:
				self.q = i
				break
		for i, val in enumerate(self.lag_pacf_1):
			if val < top_y + threshold:
				self.p = i
				break
		return self.p, self.q, self.P, self.Q

	def build_model(self):
		'''
		Uses the parameters defined in the method above and passes it in to the SARIMA model. The model is then fit and predicts future values based on input from user.
		'''
		model = sm.tsa.statespace.SARIMAX(self.time_series['Price'], trend = 'n', order = (self.p,1,self.q), seasonal_order = (self.P,1,self.Q,self.season), enforce_stationarity = False, enforce_invertibility = False)
		self.results = model.fit()
		start = self.time_series.index[-1]
		date_list = [start + relativedelta(months = x) for x in range(0,int(self.months))]
		future = pd.DataFrame(index=date_list, columns = self.time_series.columns)
		self.time_series = pd.concat([self.time_series, future])
		self.time_series['Predictions'] = self.results.predict(start = self.start, end = 2000, dynamic = True)


	def get_data_source(self):
		return self.time_series


if __name__ == '__main__':
	myinterpreter = Interpreter( 'avg_elec_price', 30)
	myinterpreter.build_model()
