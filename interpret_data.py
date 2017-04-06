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
        print(self.time_series)
        print(ts_log.shift())
        self.ts_log_diff = ts_log - ts_log.shift()

    def create_acf(self):
        print(self.ts_log_diff)
        lag_acf = acf(self.ts_log_diff,nlags=20)
        lag_pacf = pacf(self.ts_log_diff,nlages=20, method = 'ols')
        plt.subplot(121)
        plt.plot(lag_acf)
        plt.subplot(122)
        plt.plot(lag_pacf)
        plt.tight_layout




test_interpreter = Interpreter('', 'camera.txt', 'camera_data.txt',30)
myinterpreter = Interpreter('', 'phone.txt', 'phone_data.txt', 30)
test_interpreter.differencing()
test_interpreter.create_acf()
