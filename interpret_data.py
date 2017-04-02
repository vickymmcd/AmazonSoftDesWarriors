from scipy.interpolate import UnivariateSpline
from format_data import Formatter
import matplotlib.pyplot as plt
import time


class Interpreter:
    def __init__(self, url, file_name, data_file_name, n_days):
        self.formatter = Formatter(url, file_name, data_file_name)
        self.x_values, self.y_values = self.formatter.data_to_matrix()
        self.intra_x_values = []
        self.n_days = n_days
        self.n_days = self.creating_wanted_days(n_days)
        self.n_days = self.creating_wanted_days()
        self.intra_y_values = intra_y_values

    def creating_wanted_days(self):
        epoch_time = time.time()
        for day in self.n_days:
            self.intra_x_values.append(self.formatter.add_day(epoch_time))
            epoch_time = self.formatter.add_day(epoch_time)
        return self.intra_x_values

    def data_to_function(self):
        poly_func = KroghInterpolator(self.x_values,self.y_values)
        self.intra_y_values = [KroghInterpolator.__call__(self.n_days)]
        print(self.intra_y_values)
        return self.intra_x_values, self.intra_y_values

    def graph_intra_val(self):
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        p = subplot.plot(self.x_values+self.intra_x_values,self.y_values+self.intra_y_values)
        fig.show()

    def find_lowest_price(self):
        price = min(self.intra_y_values)
        dic_intra = {key:value for key, value in zip(intra_x_values, intra_y_values)}
        #returns the day
        return key for key,value in dic_intra if value == price

test_interpreter = Interpreter('', 'camera.txt', 'camera_data.txt',30)
print(test_interpreter.data_to_function)

myinterpreter = Interpreter('', 'phone.txt', 'phone_data.txt', 40)
myinterpreter.graph_intra_val()
