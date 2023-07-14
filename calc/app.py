from flask import Flask, request
from operations import add, mult, sub, div
print("hi")

app = Flask(__name__)


@app.route("/add")
def adding():
    """Returns the sum of 2 parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)


@app.route('/sub')
def subtract():
    """It subtracts the second parameter from the first"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/mult')
def multiply(a, b):
    """It returns the product of the parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/div')
def divide():
    """It divides the first parameter by the second
    """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

