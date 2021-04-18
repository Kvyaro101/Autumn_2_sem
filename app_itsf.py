import flask
from flask import Flask, request
import euclid_primary
from euclid_primary import gcd_only


app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return flask.render_template(
        'list_char.html'
    )


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/name', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        data=request.args.get('name')
    elif request.method == 'POST':
        data=request.form.get('name')

    if data is None or data[0] == 'G' or data[0] == 'N':
        return flask.render_template(
                    'name.html',
                    name="No data",
                    method=request.method
                )
    else:
        for i in range(len(data)):
            if ord(data[i]) == 32:
                space_number = i
                first, second = float(data[:space_number]), float (data[(space_number+1):])
                gcd, lcm = float(gcd_only(first, second)), first*second/float(gcd_only(first, second))
                name_param = 'GCD:'+str(gcd)+', LCM:'+str(lcm)
                return flask.render_template(
                    'name.html',
                    name=name_param,
                    method=request.method
                )

if __name__ == '__main__':
   app.run(debug = True)
