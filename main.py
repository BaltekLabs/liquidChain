from flask import Flask, request, render_template, redirect, url_for
import requests
import io
import pandas as pd
import csv

app = Flask(__name__)

# PAGE ROUTES

@app.route("/")
def index():
    return render_template('/homeLanding.html')

@app.route('/homeLanding')
def home():
    return render_template('/homeLanding.html')

@app.route('/userLanding')
def userLanding():
    return render_template('/userLanding.html')

@app.route('/stockData')
def stockData():
    return render_template('/stockData.html')

@app.route('/falseIdent')
def falseIdent():
    return render_template('/homelandingNullLogin.html')



# FORM ROUTES

@app.route('/userHome', methods=['GET','POST'])
def userHome():
    user_num = "0"
    user_name = "User"
    if request.method == 'POST':
        user_num = request.form['user_id']
        
    if user_num == "1":
            user_name = "William"
    else:
        return redirect('/falseIdent')
        
    return render_template('/userLanding.html', user_name=user_name)
        
@app.route('/stockQuote', methods=['GET','POST'])
def stockQuote():
    API_KEY = '8XTSMCVVBO5CJLT9'
    if request.method == 'POST':
        stock_request = request.form['stock_search']
        r = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s&apikey='%stock_request + API_KEY)
        with open('out.csv', 'w') as f:
            writer = csv.writer(f)
            reader = csv.reader(r.text)

            for row in reader:
                writer.writerow(row)
        
        stock_data = pd.read_csv('out.csv',error_bad_lines=False)

        
    return render_template('/stockData.html', stock_data=stock_data)



#Functions

if __name__ == "__main__":
    app.run(debug=True)
    
