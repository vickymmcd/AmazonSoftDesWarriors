import os
#import os.environ
from flask import Flask, render_template, request
from data_scrape import Collector
from bokeh.plotting import figure
from bokeh.embed import components
from visualization import Visualization
from graphing_data import Grapher
from interpreter_final import Interpreter
from socket import gethostname
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def testing():
    # html1 = Visualization.show_layout
    return render_template('testingPromo.html')
    # return render_template('graph.html', script=script, div=div)
@app.route('/result/', methods=['POST', 'GET'])
def result():
    error = None
    if request.method == 'POST':
        result = request.form
        for key, val in result.items():
            if key == 'prod':
                prod = val
                if prod == 'Oil':
                    myinterpreter = Interpreter('', '', 'oil_prices', 30)
                    myinterpreter.differencing()
                    #myinterpreter.test_stationarity()
                    myinterpreter.create_acf()
                    myinterpreter.get_p_and_q()
                    myinterpreter.build_model()
                    data = myinterpreter.get_data_source()
                    visualization = Visualization(data)
                    plot = visualization.get_graph1()
                    script, div = components(plot)
                elif prod == 'Electricity':
                    # myinterpreter = Interpreter('', '', 'avg_elec_prices', 30)
                    myinterpreter = Interpreter('', '', 'oil_prices', 30)
                    myinterpreter.differencing()
                    #myinterpreter.test_stationarity()
                    myinterpreter.create_acf()
                    myinterpreter.get_p_and_q()
                    myinterpreter.build_model()
                    data = myinterpreter.get_data_source()
                    visualization = Visualization(data)
                    plot = visualization.get_graph1()
                    script, div = components(plot)
            elif key == 'timeWindow':
                time = val
        if time == '' or prod == '':
            error = 'Please fill in all fields.'
    return render_template("result.html", prod=prod, time=time,
                         error=error, script=script, div=div)


if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
         HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
         PORT = int(os.environ.get('PORT', 5000))
         app.run(host=HOST, port=PORT)
        # app.debug = True
        # app.run()
