from format_data import Formatter
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

formatter = Formatter("", "umbrella.txt", "umbrella_data.txt")
frame = formatter.data_to_dataframe()
# frame
# plt.figure()
# plt.plot(frame)
# plt.show()

# frame = frame.drop(frame.columns[[1]], axis = 1, inplacse = True)
frame
# frame2 = frame.rolling(window = 12, center = False).mean()
decomposition = seasonal_decompose(frame, freq=365)
seasonal = decomposition.seasonal
trend = decomposition.trend
resid = decomposition.resid

plt.figure()
plt.plot(frame)
plt.plot(trend)
plt.plot(seasonal)
# plt.plot(resid)
plt.show()

