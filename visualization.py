'''
This class represents the visualization object with multiple graphs
'''
#TODO integrate this with flask website
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter, HoverTool, CategoricalColorMapper
from bokeh.layouts import column, row
from graphing_data import Grapher
from interpret_data import Interpreter
from bokeh.embed import components
import bokeh.palettes
import datetime

class Visualization:
    def __init__(self, data1, data2=None):
        '''
        This initializes the Visualization class and assigns the two
        graphs and datasets. It sets up the figures for these graphs and
        sets up the layout for them.

        data1: pandas dataframe containing price history data
        data2: pandas dataframe containing price forecast data
        '''
        self.data1 = data1
        self.data2 = data2
        self.data1.columns=['Price']
        #self.data2.columns = ['Price']
        self.data1['Datestring'] = [datetime.datetime.fromtimestamp(int(x/1000000000)).strftime('%Y-%d-%m') for x in self.data1.index.values.tolist()]
        self.find_lowest_prices()
        self.hover = HoverTool(tooltips=[('Date', '@Datestring'),('Price', '@Price'),
                                         ('Cheapest', '@Cheapest')])
        self.mapper = CategoricalColorMapper(factors=[True, False],
                                             palette=['red', 'green'])
        self.graph1 = figure(title='Price History', plot_width=900, plot_height=400, tools=[self.hover, 'pan',
                                                      'wheel_zoom'])
        self.graph2 = figure(title='Price Forecast', plot_width=900, plot_height=400)

        print(self.data1.columns)
        self.graph1.xaxis.formatter=DatetimeTickFormatter(
                hours=["%d %B %Y"],
                days=["%d %B %Y"],
                months=["%d %B %Y"],
                years=["%d %B %Y"],
            )
        self.graph2.xaxis.formatter=DatetimeTickFormatter(
                hours=["%d %B %Y"],
                days=["%d %B %Y"],
                months=["%d %B %Y"],
                years=["%d %B %Y"],
            )

        # add a line renderer
        self.graph1.line(source=self.data1, x='index', y='Price', line_width=2, line_color='green')
        self.graph1.circle(source=self.data1, size=1, x='index', y='Price', line_width=2, color={'field': 'Cheapest', 'transform': self.mapper})
        #self.graph2.line(source=self.data2, x='index', y='Price', line_width=2)
        self.layout = column(self.graph1, self.graph2)


    def get_graph1(self):
        '''
        Returns the figure for graph1 which can be used and shown
        in a layout
        '''
        return self.graph1

    def get_graph2(self):
        '''
        Returns the figure for graph2 which can be used and shown
        in a layout
        '''
        return self.get_graph2

    def get_layout(self):
        '''
        Returns the layout associated with the two graphs which
        can be accessed and used in another application
        '''
        return self.layout

    def show_layout(self):
        '''
        Sets up html file for output and shows that file
        '''
        output_file('line.html')
        show(self.layout)

    def find_lowest_prices(self):
        '''

        '''
        limit = 1.05 * min(self.data1['Price'])
        self.data1['Cheapest'] = [x <= limit for x in self.data1['Price']]


if __name__ == '__main__':
    '''
    Set up the data and pass it into the visualization object to be
    visualized
    '''
    myg = Grapher("", "umbrella.txt", "umbrella_data.txt")
    resid = myg.decompose_ts()
    original_data = myg.get_data()
    '''myint = Interpreter("", "christmas.txt", "christmas_data.txt", 30)
    myint.differencing()
    myint.create_acf()
    parimalog = myint.do_ARIMA()'''
    visualization = Visualization(original_data, resid)
    #visualization.show_layout()
    visualization.show_layout()
