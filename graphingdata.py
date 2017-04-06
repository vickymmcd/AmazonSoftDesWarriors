from format_data import Formatter
import matplotlib.pyplot as plt

formatter = Formatter("", "christmas.txt", "christmas_data.txt")
frame = formatter.data_to_dataframe()
x_values, y_values = formatter.data_to_matrix()
plt.figure()
plt.plot(frame)
plt.show()
