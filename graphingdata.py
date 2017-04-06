from format_data import Formatter
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

formatter = Formatter("", "christmas.txt", "christmas_data.txt")
frame = formatter.data_to_dataframe()

frame = frame.drop(frame.columns[[1]], axis = 1, inplace = True)
frame
# frame2 = frame.rolling(window = 12, center = False).mean()
decomposition = seasonal_decompose(frame, freq=10)
seasonal = decomposition.seasonal
trend = decomposition.trend
resid = decomposition.resid

plt.figure()
plt.plot(frame)
plt.plot(trend)
plt.plot(seasonal)
plt.plot(resid)
plt.show()