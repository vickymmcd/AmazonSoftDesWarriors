from format_data import Formatter
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from bokeh.plotting import figure, output_file, show
import pandas as pd
import numpy as np
from bokeh.palettes import Spectral11
from bokeh.plotting import figure, show, output_file

formatter = Formatter("", "christmas.txt", "christmas_data.txt")
frame = formatter.data_to_dataframe()
frame
# frame2 = frame.rolling(window = 12, center = False).mean()
decomposition = seasonal_decompose(frame, freq=365)
seasonal = decomposition.seasonal
trend = decomposition.trend
resid = decomposition.resid

output_file("test.html")

toy_df = pd.DataFrame(data=np.random.rand(5,3), columns = ('a', 'b' ,'c'), index = pd.DatetimeIndex(start='01-01-2015',periods=5, freq='d'))

numlines=len(toy_df.columns)
mypalette=Spectral11[0:numlines]

p = figure(width=500, height=300, x_axis_type="datetime")
p.multi_line(xs=[toy_df.index.values]*numlines,
                ys=[toy_df[name].values for name in toy_df],
                line_color=mypalette,
                line_width=5)
show(p)


"""
OTHER OPTION! TIMESERIES PLOTTTT!!!
import pandas as pd
from bokeh.charts import TimeSeries, output_file, show

AAPL = pd.read_csv(
        "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
        parse_dates=['Date'])

output_file("timeseries.html")

data = dict(AAPL=AAPL['Adj Close'], Date=AAPL['Date'])

p = TimeSeries(data, index='Date', title="APPL", ylabel='Stock Prices')

show(p)
"""




'''
### matplotlib plotter ###
plt.figure()
plt.plot(frame)
plt.plot(trend)
plt.plot(seasonal)
# plt.plot(resid)
plt.show()
'''
