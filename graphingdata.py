from format_data import Formatter
import matplotlib.pyplot as plt

formatter = Formatter("", "christmas.txt", "christmas_data.txt")
x_values, y_values = formatter.data_to_matrix()
plt.figure()
plt.plot(x_values,y_values,"ro")
plt.show()
