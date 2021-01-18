from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes


app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenz123"
c = CurrencyRates()
code = CurrencyCodes()

@app.route('/')
def home_form():
    return render_template('form.html')

@app.route('/next', methods=["POST"])
def form_data():
    convert_from = request.form['convert_from'] 
    convert_to = request.form['convert_to'] 
    amount = request.form['amount'] 

    # Creates an object with availble rates used to see if currencies exist 
    currencies = c.get_rates('USD')

    # try/except to make sure input amount looks like a number
    try:
        float(amount)
    except:
        flash("The amount you have entered is not a number", "error")
        return redirect('/home')

    # if convert from input is not valid currency code
    if(currencies.get(convert_from) is None):
        flash(f"Tried to convert from: '{convert_from}', which is not a valid code.", "error")
        return redirect('/home')

    # if convert to input is not valid currency code
    elif(currencies.get(convert_to) is None):
        flash(f"Tried to convert to: '{convert_to}', which is not a valid code", "error")
        return redirect('/home')

     # if amount is a negative number
    elif(float(amount) < 0):
        flash("Please enter a positive number for amount", "error")
        return redirect('/home')
    
    else:
        rate = c.get_rate(convert_from, convert_to)
        result = round(float(rate) * float(amount), 2)
        symbol = code.get_symbol(convert_to)
        return render_template ('result.html', result=result, symbol=symbol)

     


@app.route('/home')
def return_home():
    return redirect('/')