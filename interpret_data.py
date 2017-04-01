from scipy.interpolate import UnivariateSpline
from format_data import Formatter
import matplotlib.pyplot as plt

class interpret_data:
    def __init__(self,url,file_name,data_file_name,n_days):
        self.formatter = Formatter(url,file_name,data_file_name)
        self.x_values, self.y_values = Formatter.data_to_matrix()
        self.intra_x_values = []
        self.n_days = n_days
        self.n_days = creating_wanted_days(30)
        self.intra_y_values = intra_y_values

    def creating_wanted_days():
        epoch_time= time.time()
        self.intra_x_values = [Formatter.add_day(epoch_time) for day in self.n_days]
        return self.intra_x_values

    def data_to_function():
        poly_func = KroghInterpolator(self.x_values,self.y_values)
        self.intra_y_values = [KroghInterpolator.__call__(self.n_days)]
        print(self.intra_y_values)
        return self.intra_x_values, self.intra_y_values

    def graph_intra_val():
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        p = subplot.plot(self.x_values+self.intra_x_values,self.y_values+self.intra_y_values)
        fig.show()

    def find_lowest_price():
        price = min(self.intra_y_values)
        