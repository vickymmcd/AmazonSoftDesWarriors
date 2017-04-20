from flask import Flask, render_template, request
from data_scrape import Collector
from bokeh.embed import components
from visualization import Visualization
from graphing_data import Grapher
from socket import gethostname
app = Flask(__name__)


@app.route('/')
def hello_world():
    myg = Grapher("", "christmas.txt", "christmas_data.txt")
    #resid = myg.decompose_ts()
    original_data = myg.get_data()
    myvis = Visualization(original_data)
    plot = myvis.get_graph1()
    script, div = components(plot)
    return render_template('index.html', script=script, div=div)


@app.route('/test')
def testing():
    script, div = components(plot)
    return render_template('graph.html', script=script, div=div)


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
                myg = Grapher('', filename, filedataname)
                #resid = myg.decompose_ts()
                original_data = myg.get_data()
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
