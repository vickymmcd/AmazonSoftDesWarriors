from flask import Flask, render_template, request
from data_scrape import Collector
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def testing():
    return render_template('dropdown.html')


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
