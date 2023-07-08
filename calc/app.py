from flask import Flask
from operations import *


app = flask(__name__)


@app.route('/add')
def adding():
    """Returns the sum of 2 parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))


@app.route('/subtract')
def subtract():
    """It subtracts the second parameter from the first"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/multiply')
def multiply(a, b):
    """It returns the product of the parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/divide')
def divide():
    """It divides the first parameter by the second
    """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return div(a, b)