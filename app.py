"""
converter
"""

from flask import Flask, request, render_template, redirect, url_for, session
import requests
import ctypes

app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            amount = float(amount)
            from_box = request.form['from_c']
            to_box = request.form['to_c']

            data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
            currencies = data["rates"]

            rate = float("rates")
            result = rate * amount

            return render_template('home.html', result=round(result, 2), amount=amount,
                                   from_box=from_box, from_box = from_box, 
                                   to_box=to_box, to_box=to_box)
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
  
    else:
        return render_template('currency.html')
  
  
if __name__ == "__main__":
    app.run(debug=True)