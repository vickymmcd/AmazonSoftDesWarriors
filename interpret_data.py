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
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima_model import ARIMA



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

        self.x_values =[]
        min_val = min(np_to_list[1:])
        for x in np_to_list:
        	x = x - min_val
        	self.x_values.append(x)
        self.lag_acf = acf(self.x_values[1:],nlags=20)
        self.lag_pacf = pacf(self.x_values[1:],nlags=20, method = 'ols')
        #for a 95% confidence interval
        #Plot ACF:
        plt.subplot(121)
        plt.plot(self.lag_acf)
        plt.axhline(y=0,linestyle='--',color='gray')
        plt.axhline(y=-1.65/np.sqrt(len(self.x_values)),linestyle='--',color='gray')
        plt.axhline(y=1.65/np.sqrt(len(self.x_values)),linestyle='--',color='gray')
        plt.title('Autocorrelation Function')

        plt.subplot(122)
        plt.plot(self.lag_pacf)
        plt.axhline(y=0,linestyle='--',color='gray')
        plt.axhline(y=-1.65/np.sqrt(len(self.x_values)),linestyle='--',color='gray')
        plt.axhline(y=1.65/np.sqrt(len(self.x_values)),linestyle='--',color='gray')
        plt.title('Partial Autocorrelation Function')
        plt.tight_layout()
        plt.show()

    def do_ARIMA(self):
        '''
        Sets up and graphs the ARIMA forecasting for the time series
        '''
        # Find intersection with the top line for each graph
        threshold = .03
        top_y = 1.65/np.sqrt(len(self.x_values))
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
        model = ARIMA(self.ts_log, order=(p, 1, q))
        results_ARIMA = model.fit(disp=-1)
        plt.plot(self.ts_log_diff)
        plt.plot(results_ARIMA.fittedvalues, color='red')
        plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-self.ts_log_diff)**2))
        plt.show()



myinterpreter = Interpreter('', 'christmas.txt', 'christmas_data.txt', 30)
myinterpreter.differencing()
myinterpreter.create_acf()
