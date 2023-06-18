#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<para>')
def print_string(para):
    print(para)
    return para


@app.route('/count/<int:parameter>')
def count_route(parameter):
    count = ""
    for i in range(int(parameter)):
        count += str(i) + "\n"
    return count


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '-':
        calc = int(num1) - int(num2)
        return str(calc)
    elif operation == '+':
        calc = int(num1) + int(num2)
        return str(calc)
    elif operation == '*':
        calc = int(num1) * int(num2)
        return str(calc)
    elif operation == 'div':
        calc = int(num1) / int(num2)
        return str(calc)
    elif operation == '%':
        calc = int(num1) % int(num2)
        return str(calc)
    else:
        return ('Invalid operation')


if __name__ == '__main__':
    app.run(port=5555)
    # debug=True
