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
        self.x_values, self.y_values = self.formatter.data_to_matrix()
        self.intra_x_values = []
        self.n_days = n_days
        self.creating_wanted_days()
        self.intra_y_values = []

    def creating_wanted_days(self):
        epoch_time = time.time() * 1000
        #print(self.x_values)
        #print(self.y_values)
        for day in range(self.n_days):
            self.intra_x_values.append(self.formatter.add_day(epoch_time))
            epoch_time = self.formatter.add_day(epoch_time)
        return self.intra_x_values

    def data_to_function(self):
        '''
        Uses the KroghInterpolator to make a function from our
        data and uses that function to predict the prices at
        the wanted dates.

        returns: wanted dates (self.intra_x_values)
        and their associated predicted prices (self.intra_y_values)
        '''
        print(self.x_values)
        print(self.y_values)
        poly_func = KroghInterpolator(self.x_values,self.y_values)
        self.creating_wanted_days(self.n_days)
        #self.intra_x_values= [1477492378020,1477492378030]
        #self.intra_x_values = self.intra_x_values[:-1]
        self.intra_x_values = np.asarray(self.intra_x_values)
        print(self.intra_x_values)
        self.intra_y_values = poly_func.__call__(self.intra_x_values)
        print(self.intra_y_values)
        return self.intra_x_values, self.intra_y_values

    def do_the_svm(self):
        self.func = svm.SVR(kernel='poly')
        self.func.fit(np.array(self.x_values).reshape(-1,1),np.ravel(np.array(self.y_values).reshape(-1,1)))
        print(self.func.predict(np.array(self.intra_x_values).reshape(-1,1)))

    def do_linear_regression(self):
        regr = linear_model.LinearRegression()
        train_data_X = map(lambda x: [self.x_values], list(self.x_values))
        train_data_Y = list(self.y_values)
        regr.fit(np.array(self.x_values).reshape(-1,1),np.array(self.y_values).reshape(-1,1))
        print(self.y_values)
        a= np.array(self.intra_x_values).reshape(-1,1)
        print(regr.predict(a))

    def make_poly_model(self):
        poly_model = make_pipeline(PolynomialFeatures(3),
                           LinearRegression())
        poly_model.fit(np.array(self.x_values).reshape(-1,1),np.array(self.y_values).reshape(-1,1))
        print(poly_model.predict(np.array(self.intra_x_values).reshape(-1,1)))

    def graph_intra_val(self):
        #self.data_to_function()
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        p = subplot.plot(self.x_values+self.intra_x_values,self.y_values+self.intra_y_values[0])
        fig.show()

    def find_lowest_price(self):
        price = min(self.intra_y_values)
        dic_intra = {key:value for key, value in zip(intra_x_values, intra_y_values)}
        #returns the day

        return [key for key,value in dic_intra if value == price]


test_interpreter = Interpreter('', 'camera.txt', 'camera_data.txt',30)
myinterpreter = Interpreter('', 'phone.txt', 'phone_data.txt', 30)
myinterpreter.make_poly_model()
