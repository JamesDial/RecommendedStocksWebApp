'''
Unit testing for models.py - 99% coverage achieved
Author: Ethan Kenny
Run command in terminal to generate coverage report:
    pytest src/app/test/models_test.py --cov --cov-branch --cov-report html
'''

import pytest
from app.models import Investor, Stock, Crypto, Watchlist, stocks_crypto_by_risk

class TestSurvey:

    def test_investor_class(self):
        first_name = "Joe"
        last_name = "Smith"
        email = "joesmith@aol.com"
        password = "password1234"

        investor = Investor(first_name, last_name, email, password)

        assert repr(investor) == "FirstName:{}\tLastName:{}\tUserEmail:{}\tPassword:{}" \
                                 .format(investor.firstName, investor.lastName, investor.userEmail, investor.password)

    def test_stock_class(self):
        name = "Apple"
        symbol = "AAPL"
        price = 123.45

        stock = Stock(name, symbol, price)

        assert repr(stock) == "Name:{}\tSymbol:{}\tPrice:{}\t".format(stock.Name, stock.Symbol, stock.Price)

    def test_crypto_class(self):
        name = "Bitcoin"
        symbol ="BTC"
        price = 50000.01

        coin = Crypto(name, symbol, price)

        assert repr(coin) == "Name:{}\tSymbol:{}\tPrice:{}".format(coin.Name, coin.Symbol, coin.Price)

    def test_watchlist_class(self):
        email = "joesmith@gmail.com"
        name = "Amazon"
        symbol = "AMZN"
        price = 12345.67
        type = "Stock"

        watch = Watchlist(email, name, symbol, price, type)

        assert repr(watch) == "userEmail:{}\tName:{}\tSymbol:{}\tPrice:{}\tType:{}" \
                              .format(watch.userEmail, watch.name, watch.symbol, watch.price, watch.type)

    def test_stocks_crypto_by_risk_class(self):
        name = "Microsoft"
        symbol = "MSFT"
        price = 3.50
        type = "Stock"
        risk = "Medium"

        msft_risk = stocks_crypto_by_risk(name, symbol, price, type, risk)

        assert repr(msft_risk) == "Name:{}\tSymbol:{}\tPrice:{}\tType:{}\tRisk:{}"\
               .format(msft_risk.name, msft_risk.symbol, msft_risk.price, msft_risk.type, msft_risk.risk)
