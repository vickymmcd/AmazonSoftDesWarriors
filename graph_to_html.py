from format_data import Formatter
import matplotlib.pyplot as plt, mpld3

formatter = Formatter("", "christmas.txt", "christmas_data.txt")
frame = formatter.data_to_dataframe()
x_values, y_values = formatter.data_to_matrix()
fig = plt.plot(frame)
plt.show()
savedHtml = mpld3.fig_to_html(fig, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False)
#bokeh plot look into it sam.
