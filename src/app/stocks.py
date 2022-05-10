import copy

import app.ufi_database as database
from flask import render_template, Blueprint, redirect, url_for, flash, request
from app.models import Investor, Stock, Crypto, Watchlist, stocks_crypto_by_risk
from operator import attrgetter
from app import db
from flask_login import current_user


class StockObject:
    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price

class CryptoObject:
    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price

# do on favorites page
#   BEFORE PUSH, DELETE DEFAULT=NULL IN MODELS.PY LINE 23
def get_stocks_crypto_by_risk(email):
    stock_list = []
    crypto_list = []
    all_stocks = []
    all_crypto = []

    query = Stock.query.order_by("Name")
    for i in query:
        all_stocks.append(StockObject(i.Symbol,i.Name,i.Price))
    query = Crypto.query.order_by("Name")
    for i in query:
        all_crypto.append(i)

    # make a check to see if the investor has a risk level, otherwise, tell them to take the survey
    if current_user.riskLevel == 'NULL':
        flash("Take the survey to get your risk level")
    elif current_user.riskLevel == 'Low':
        query = stocks_crypto_by_risk.query.filter_by(type="Stock", risk="Low")
        for i in query:
            stock_list.append(StockObject(i.symbol, i.name, i.price))
        query = stocks_crypto_by_risk.query.filter_by(type="Crypto", risk="Low")
        for i in query:
            crypto_list.append(CryptoObject(i.symbol, i.name, i.price))
    elif current_user.riskLevel == 'Medium':
        query = stocks_crypto_by_risk.query.filter_by(type="Stock", risk="Medium")
        for i in query:
            stock_list.append(StockObject(i.symbol, i.name, i.price))
        query = stocks_crypto_by_risk.query.filter_by(type="Crypto", risk="Medium")
        for i in query:
            crypto_list.append(CryptoObject(i.symbol, i.name, i.price))
    elif current_user.riskLevel == 'High':
        query = stocks_crypto_by_risk.query.filter_by(type="Stock", risk="High")
        for i in query:
            stock_list.append(StockObject(i.symbol, i.name, i.price))
        query = stocks_crypto_by_risk.query.filter_by(type="Crypto", risk="High")
        for i in query:
            crypto_list.append(CryptoObject(i.symbol, i.name, i.price))


    stock_list_copy = copy.deepcopy(stock_list)
    crypto_list_copy = copy.deepcopy(crypto_list)
    all_stocks_copy = copy.deepcopy(all_stocks)
    all_crypto_copy = copy.deepcopy(all_crypto)

    stock_list_copy.sort(key=attrgetter('price'))
    stock_list_price_asc = copy.deepcopy(stock_list_copy)
    crypto_list_copy.sort(key=attrgetter('price'))
    crypto_list_price_asc = copy.deepcopy(crypto_list_copy)

    stock_list_copy.sort(key=attrgetter('price'), reverse=True)
    stock_list_price_desc = copy.deepcopy(stock_list_copy)
    crypto_list_copy.sort(key=attrgetter('price'), reverse=True)
    crypto_list_price_desc = copy.deepcopy(crypto_list_copy)

    stock_list_copy.sort(key=attrgetter('name'))
    stock_list_alpha = copy.deepcopy(stock_list_copy)
    crypto_list_copy.sort(key=attrgetter('name'))
    crypto_list_alpha = copy.deepcopy(crypto_list_copy)

    stock_list_copy.sort(key=attrgetter('name'), reverse=True)
    stock_list_rev_alpha = copy.deepcopy(stock_list_copy)
    crypto_list_copy.sort(key=attrgetter('name'), reverse=True)
    crypto_list_rev_alpha = copy.deepcopy(crypto_list_copy)

    stock_list_copy.sort(key=attrgetter('symbol'))
    stock_list_alpha_sym = copy.deepcopy(stock_list_copy)
    crypto_list_copy.sort(key=attrgetter('symbol'))
    crypto_list_alpha_sym = copy.deepcopy(crypto_list_copy)

    stock_list_copy.sort(key=attrgetter('symbol'), reverse=True)
    stock_list_rev_alpha_sym = copy.deepcopy(stock_list_copy)
    crypto_list_copy.sort(key=attrgetter('symbol'), reverse=True)
    crypto_list_rev_alpha_sym = copy.deepcopy(crypto_list_copy)


    return render_template('dashboard.html', len=len(stock_list), len2=len(crypto_list),
                           stock_list=stock_list, crypto_list=crypto_list,
                           all_stocks_copy=all_stocks_copy, all_crypto_copy=all_crypto_copy,
                           stock_list_price_asc=stock_list_price_asc, stock_list_price_desc=stock_list_price_desc,
                           crypto_list_price_asc=crypto_list_price_asc, crypto_list_price_desc=crypto_list_price_desc,
                           stock_list_alpha=stock_list_alpha, stock_list_rev_alpha=stock_list_rev_alpha,
                           crypto_list_alpha=crypto_list_alpha, crypto_list_rev_alpha=crypto_list_rev_alpha,
                           stock_list_alpha_sym=stock_list_alpha_sym, stock_list_rev_alpha_sym=stock_list_rev_alpha_sym,
                           crypto_list_alpha_sym=crypto_list_alpha_sym, crypto_list_rev_alpha_sym=crypto_list_rev_alpha_sym)


"""
This method returns a list of recommended stock investments for the user. It raises an exception if the user does not exist.
:param user: the User object for whom you want to get the data from the questionnaire for the recommended stock investments.
:return: a List of recommended stock investments or an empty list if the user didn't complete the questionnaire
"""

# if __name__ == '__main__':
#     app.run(debug=True)

# pass
# take data from stock API and print list to the HTML
# results of survey equal a total score. Different scores call for different stocks.
# print different list based on different scores.
# to sort, have user click a button. print sorted based on the button they press.

