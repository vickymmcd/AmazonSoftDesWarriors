from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
from bokeh.layouts import column, row
from graphing_data import Grapher
from interpret_data import Interpreter

myg = Grapher("", "christmas.txt", "christmas_data.txt")
resid = myg.decompose_ts()
original_data = myg.graph_data()
myint = Interpreter("", "christmas.txt", "christmas_data.txt", 30)
myint.differencing()
myint.create_acf()
parimalog = myint.do_ARIMA()
output_file("line.html")

p = figure(plot_width=900, plot_height=400)
p2 = figure(plot_width=900, plot_height=400)

resid.columns=['Price']
original_data.columns = ['Price']
print(original_data)

p.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )
p2.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )

# add a line renderer
p.line(source=resid, x='index', y='Price', line_width=2)
p2.line(source=original_data, x='index', y='Price', line_width=2)

layout = column(p, p2)
show(layout)
