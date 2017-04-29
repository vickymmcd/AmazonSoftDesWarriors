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
<<<<<<< HEAD
=======
    myg = Grapher("", "christmas.txt", "more_christmas_data.txt")
    #resid = myg.decompose_ts()

>>>>>>> f09a42dfac1790ef129612073461076f71a4c81d
    return render_template('testingPromo.html')


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
                filename = '' + prod + '.txt'
                print(filename)
                filedataname = 'more_' + prod + '_data.txt'
                print(filedataname)

                collect = Collector('', filename, filedataname)
                # prod = collect.get_id()
                print(prod)
                myg = Interpreter('', filename, filedataname, 30)
                #resid = myg.decompose_ts()
                original_data = myg.get_data_source()

                myvis = Visualization(original_data)
                plot = myvis.get_graph1()
                script, div = components(plot)
            elif key == 'timeWindow':
                time = val
            elif key == 'where':
                where = val
        if time == '' or prod == '' or where == '':
            error = 'Please fill in all fields.'
    return render_template("result.html", prod=prod, time=time,
                           where=where, error=error, script=script, div=div)


if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run()
