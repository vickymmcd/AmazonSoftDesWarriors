from flask import Flask, render_template, request
from data_scrape import Collector
from bokeh.plotting import figure
from bokeh.embed import components
from visualization import Visualization
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def testing():
    # html1 = Visualization.show_layout
    return render_template('graph.html')
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
                filedataname = '' + prod + '_data.txt'
                print(filedataname)

                collect = Collector('', filename, filedataname)
                prod = collect.get_id()
                print(prod)
            elif key == 'timeWindow':
                time = val
            elif key == 'where':
                where = val
        if time == '' or prod == '' or where == '':
            error = 'Please fill in all fields.'
    return render_template("result.html", prod=prod, time=time,
                           where=where, error=error)


if __name__ == '__main__':
    app.run()
