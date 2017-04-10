from format_data import Formatter
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


class grapher:
    '''
    contains functions and classes to graph time series
    '''
    def __init__(self, url, file_name, data_file_name):
        self.ts_data = Formatter(url, file_name, data_file_name)
        self.ts.frame = self.ts_data.data_to_dataframe()

    def decompose_ts(self):
        self.ts.decomposition = seasonal_decompose(self.ts.frame, freq=365)
        self.seasonal = self.ts.decomposition.seasonal
        self.trend = self.ts.decomposition.trend
        self.resid = self.ts.decomposition.resid

    def graph_data(self):
        pass

# from bokeh.charts import Line, show, output_file
formatter = Formatter("", "christmas.txt", "christmas_data.txt")
frame = formatter.data_to_dataframe()
decomposition = seasonal_decompose(frame, freq=365)
seasonal = decomposition.seasonal
trend = decomposition.trend
resid = decomposition.resid

plt.figure()
#plt.plot(frame)
#plt.plot(trend)
#plt.plot(seasonal)
plt.plot(resid)
print(resid.dropna())
plt.show()
