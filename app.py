from flask import Flask , render_template , request

import model as m

app = Flask(__name__, static_folder='static')

import numpy as np

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        # Get the form data and make a prediction
        MarketCapture = float(request.form['MarketCapture'])
        PERatio = float(request.form['PERatio'])
        Dividend = float(request.form['Dividend'])
        PromoterHoldings = float(request.form['PromoterHoldings'])
        ProfitGrowth = float(request.form['ProfitGrowth'])
        SalesGrowth = float(request.form['SalesGrowth'])
        ROCE = float(request.form['ROCE'])

        result = m.predict_stock(MarketCapture, PERatio, Dividend, PromoterHoldings, ProfitGrowth, SalesGrowth, ROCE)

        if result==0:
            result = "Fundamentally Weak"
        elif result==1:
            result = "Fundamentally Strong"
        # Pass the result to the template
        return render_template("index.html", result=result)
    else:
        # Render the form
        return render_template("index.html")
    


if __name__ == "__main__":
    app.run(debug=True)