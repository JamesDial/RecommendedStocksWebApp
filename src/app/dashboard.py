from flask import render_template
from app.models import stocks_crypto_by_risk, Investor

# stock_list_low_risk = []
# stock_list_medium_risk = []
# stock_list_high_risk = []
from sqlalchemy.sql.elements import Null

stock_list = []
# do on favorites page

def get_stocks_by_risk(current_user):
    # make a check to see if the investor has a risk level, otherwise, tell them to take the survey
    if Investor.filter_by(current_user).riskLevel is Null:
        stock_list.append("Take the survey to get your risk level")
    else:
        query = stocks_crypto_by_risk.query.filter_by(type="Stock", risk="Low")
        for i in query:
            stock_list.append(i)

        query = stocks_crypto_by_risk.query.filter_by(type="Stock", risk="Medium")
        for i in query:
            stock_list.append(i)

        query = stocks_crypto_by_risk.query.filter_by(type="Stock", risk="High")
        for i in query:
            stock_list.append(i)


    return render_template('dashboard.html', stock_list=stock_list)#stock_list_low_risk=stock_list_low_risk,
                                            #stock_list_medium_risk=stock_list_medium_risk,
                                            #stock_list_high_risk=stock_list_high_risk)
