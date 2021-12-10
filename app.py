"""
converter
"""

from flask import Flask, request, render_template, redirect, url_for, session
import requests
import ctypes

app = Flask(__name__)

currencies = data["rates"]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            amount = float(amount)
            from_c = request.form['from_c']
            to_c = request.form['to_c']

            data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
            currencies = data["rates"]

            rate = float(rate)
            result = rate * amount

            return render_template('home.html', result=round(result, 2), amount=amount,
                                   from_c_code=from_c_code, from_c_name=from_c_name,
                                   to_c_code=to_c_code, to_c_name=to_c_name, time=time)
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
  
    else:
        return render_template('home.html')
  
  
if __name__ == "__main__":
    app.run(debug=True)