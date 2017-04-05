from scipy.interpolate import UnivariateSpline
from scipy.interpolate import KroghInterpolator
from format_data import Formatter
import matplotlib.pyplot as plt
import time
import numpy as np

class Interpreter:
    def __init__(self, url, file_name, data_file_name, n_days):
        self.formatter = Formatter(url, file_name, data_file_name)
        self.x_values, self.y_values = self.formatter.data_to_matrix()
        self.intra_x_values = []
        self.n_days = n_days
        #self.n_days = self.creating_wanted_days(n_days)
        #self.creating_wanted_days()
        self.intra_y_values = []

    def creating_wanted_days(self,days):
        epoch_time = time.time() * 1000
        #print(self.x_values)
        #print(self.y_values)
        for day in range(self.n_days):
            self.intra_x_values.append(self.formatter.add_day(epoch_time))
            epoch_time = self.formatter.add_day(epoch_time)
        return self.intra_x_values

    def data_to_function(self):
        print(self.x_values)
        poly_func = KroghInterpolator(self.x_values,self.y_values)
        self.creating_wanted_days(self.n_days)
        #self.intra_x_values= [1477492378020,1477492378030]
        #self.intra_x_values = self.intra_x_values[:-1]
        self.intra_x_values = np.asarray(self.intra_x_values)
        print(self.intra_x_values)
        self.intra_y_values = poly_func.__call__(self.intra_x_values)
        #self.intra_y_values = [poly_func.__call__(self.intra_x_values)]
        print(self.intra_y_values)
        return self.intra_x_values, self.intra_y_values

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
        for key,value in dic_intra:
            if value == price:
                return key

test_interpreter = Interpreter('', 'camera.txt', 'camera_data.txt',30)
myinterpreter = Interpreter('', 'phone.txt', 'phone_data.txt', 30)
myinterpreter.data_to_function()
#myinterpreter.graph_intra_val()

#myinterpreter.graph_intra_val()
print(test_interpreter.data_to_function)
