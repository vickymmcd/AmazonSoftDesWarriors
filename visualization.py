'''
This class represents the visualization object with multiple graphs
'''
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter, HoverTool, CategoricalColorMapper, Range1d
from bokeh.layouts import column, row
from interpreter_final import Interpreter
from bokeh.embed import components
import bokeh.palettes
import datetime
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components
from bokeh.models import ColumnDataSource, Range1d, Plot, LinearAxis, Grid
from bokeh.models.glyphs import ImageURL


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
        self.data1['Datestring'] = [datetime.datetime.fromtimestamp(int(x/1000000000)).strftime('%B %d, %Y') for x in self.data1.index.values.tolist()]
        self.find_lowest_prices()
        self.hover = HoverTool(tooltips = [('Date', '@Datestring'),('Price', '@Price'),
                                         ('Cheapest', '@Cheapest')])
        self.hover2 = HoverTool(tooltips = [('Date', '@Datestring'),('Price', '@Predictions'),
                                         ('Cheapest', '@Cheapest2')])
        self.mapper = CategoricalColorMapper(factors=[True, False],
                                             palette=[ '#99CCFF', '#CC99FF'])
        self.graph1 = figure(title='Price History and Price Prediction', plot_width=900, plot_height=400, tools=[self.hover, 'pan',
                                                      'wheel_zoom', 'zoom_in'])
        self.graph2 = figure(title='Price Forecast', plot_width=900, plot_height=400, tools=[self.hover2, 'pan',
                                                      'wheel_zoom', 'zoom_in'])

        self.graph1.xaxis.formatter=DatetimeTickFormatter(
                hours = ['%d %B %Y'],
                days = ['%d %B %Y'],
                months = ['%d %B %Y'],
                years = ['%d %B %Y'],
            )
        self.graph2.xaxis.formatter=DatetimeTickFormatter(
                hours = ['%d %B %Y'],
                days = ['%d %B %Y'],
                months = ['%d %B %Y'],
                years = ['%d %B %Y'],
            )

        dates = (list(self.data1.index))
        self.graph2.x_range = Range1d(datetime.datetime.now(), dates[-1])

        self.graph1.line(source = self.data1, x = 'index', y = 'Price', line_width = 2, line_color = 'blue')
        self.graph1.circle(source = self.data1, size = 1, x = 'index', y = 'Price', line_width = 2, color = {'field': 'Cheapest', 'transform': self.mapper})
        self.graph1.line(source = self.data1, x = 'index', y = 'Predictions', line_width = 2, line_color = 'red')
        self.graph2.line(source = self.data1, x = 'index', y = 'Predictions', line_width = 2, line_color = 'red')
        self.graph2.circle(source = self.data1, size = 15, x = 'index', y = 'Predictions', line_width = 2, color = {'field': 'Cheapest2', 'transform': self.mapper})
        self.layout = column(self.graph1, self.graph2)

    def get_graph1(self):
        '''
        Returns the figure for graph1 which can be used and shown
        in a layout
        '''
        return self.graph1

    def get_components(self):
        '''
        Returns the components of the graph ready to be used for html
        '''
        script, div = components(self.graph1)

    def get_HTML_graph(self):
        '''
        Produces and returns the html for the bokeh graph
        '''
        html = file_html(self.graph1, CDN, 'tesingGraph1')
        return html

    def get_graph2(self):
        '''
        Returns the figure for graph2 which can be used and shown
        in a layout
        '''
        return self.graph2

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
        output_file('graph.html')
        show(self.layout)

    def find_lowest_prices(self):
        '''
        Finds date where the price is within 5% of the lowest price, and return
        a list of the cheapest dates
        '''
        limit = 1.05 * min(self.data1['Price'])
        self.data1['Cheapest'] = [x <= limit for x in self.data1['Price']]
        limit = 1.05 * min(self.data1['Predictions'].dropna())
        self.data1['Cheapest2'] = [x <= limit for x in self.data1['Predictions']]
        cheapest_dates = []
        for month_index,month in enumerate(self.data1['Cheapest2']):
            if month == True:
                cheapest_dates.append(self.data1['Datestring'][month_index])
        dates = 'The best dates to buy your product are  '
        for i,o in enumerate(cheapest_dates):
            if i == 0:
                dates = dates + cheapest_dates[i]
            else:
                dates = dates + ' , '+ cheapest_dates[i]
        return dates


if __name__ == '__main__':
    '''
    Set up the data and pass it into the visualization object to be
    visualized
    '''
    myinterpreter = Interpreter('oil_prices', 365)
    myinterpreter.differencing()
    myinterpreter.create_acf()
    myinterpreter.get_p_and_q()
    myinterpreter.build_model()
    data = myinterpreter.get_data_source()
    visualization = Visualization(data)
    visualization.show_layout()
