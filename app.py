from flask import Flask               #initially code was not run so 
from flask import request             # step1 - left hand side 3line - new terminal - pip install flask - python app.py(filename)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"


@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"


@app.route("/test")
def test():
    a = 5 + 6
    return "this is my function to run app{}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.arg.get('x')
    return "this is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
