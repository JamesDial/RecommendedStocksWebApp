from flask import render_template, flash, request, session

import app.login_and_signup as login_and_signup
import app.stocks as stocks
import app.ufi_database as database
import app.dashboard as dashboard
from app import app
from app import db
from flask_login import current_user
from app.models import Investor, Stock, Crypto, Watchlist, stocks_crypto_by_risk
from newsapi.newsapi_client import NewsApiClient
newsapi = NewsApiClient(api_key='aa6e9533f16f4f2fadea15925049c032')

@app.route('/')
def welcome_page():
    return render_template("welcome_page.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Hand off processing to the login_and_signup component.
    return login_and_signup.login()

@app.route('/logout')
def logout():
    # Hand off processing to the login_and_signup component.
    return login_and_signup.logout()

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Hand off processing to the login_and_signup component.
    return login_and_signup.register()


@app.route('/stocks')
def show_stocks():
    # Hand off to the stocks component.
    return stocks.get_stock_list()


@app.route('/dashboard')
def dashboard():
    # You should hand this off to a component rather than render_template directly.
    # Hand off to the stocks component.
    # return stocks.get_stock_list()
    return stocks.get_stocks_crypto_by_risk(current_user.userEmail)


@app.route('/resetdb')
def reset_db():
    # This is a utility method for developers.
    # Tell the database to clear data and reinitialize.
    database.reset()
    flash('Database has been reset')
    return render_template("welcome_page.html")

@app.route('/fav', methods=['GET', 'POST'])
def fav():
    # favList = []
    # crypto = []
    # allStock = []
    # allCrypto = []
    watchList = []

    if request.method == 'POST':
        email = current_user.userEmail
        stockList = request.form.getlist("stock_name")
        cryptoList = request.form.getlist("crypto_name")
        allStocksList = request.form.getlist("all_stock_name")
        allCryptosList = request.form.getlist("all_crypto_name")

        for stocks in stockList:
            query = Stock.query.filter_by(Symbol=stocks)
            for stockInfo in query:
                name = stockInfo.Name
                symbol = stockInfo.Symbol
                price = stockInfo.Price
                currStock = Stock(name,symbol,price)
                database.addWatchlist(email,name,symbol,price,type="Stock")

        for cryptos in cryptoList:
            query = Crypto.query.filter_by(Symbol=cryptos)
            for cryptoInfo in query:
                cryptoName = cryptoInfo.Name
                cryptoSymbol = cryptoInfo.Symbol
                cryptoPrice = cryptoInfo.Price
                currCrypto = Crypto(cryptoName,cryptoSymbol,cryptoPrice)
                database.addWatchlist(email,cryptoName,cryptoSymbol,cryptoPrice,type="Crypto")

        for allStocks in allStocksList:
            query = Stock.query.filter_by(Symbol=allStocks)
            for stockInfo in query:
                name = stockInfo.Name
                symbol = stockInfo.Symbol
                price = stockInfo.Price
                currStock = Stock(name, symbol, price)
                database.addWatchlist(email, name, symbol, price, type="Stock")

        for allCryptos in allCryptosList:
            query = Crypto.query.filter_by(Symbol=allCryptos)
            for cryptoInfo in query:
                cryptoName = cryptoInfo.Name
                cryptoSymbol = cryptoInfo.Symbol
                cryptoPrice = cryptoInfo.Price
                currCrypto = Crypto(cryptoName,cryptoSymbol,cryptoPrice)
                database.addWatchlist(email,cryptoName,cryptoSymbol,cryptoPrice,type="Crypto")

        query = Watchlist.query.order_by("name")
        for i in query:
            filt = Watchlist.query.filter_by(name=i.name)
            for j in filt:
                name = j.name
                symbol = j.symbol
                price = j.price
                type = j.type
                if type == "Stock":
                    currStock = Stock(name, symbol, price)
                    if not findStock(watchList,currStock):
                        watchList.append(currStock)

                elif type == "Crypto":
                    currCrypto = Crypto(name,symbol,price)
                    if not findStock(watchList,currCrypto):
                        watchList.append(currCrypto)



    # return render_template("Favorites.html", favorites=favList, crypto=crypto,
    #                        allStock=allStock, allCrypto=allCrypto)
    return render_template("Favorites.html", watchList=watchList)

def findStock(lst,target):
    for i in lst:
        if i == target:
            return True
    return False




def get_sources_and_domains():
	all_sources = newsapi.get_sources()['sources']
	sources = []
	domains = []
	for e in all_sources:
		id = e['id']
		domain = e['url'].replace("http://", "")
		domain = domain.replace("https://", "")
		domain = domain.replace("www.", "")
		slash = domain.find('/')
		if slash != -1:
			domain = domain[:slash]
		sources.append(id)
		domains.append(domain)
	sources = ", ".join(sources)
	domains = ", ".join(domains)
	return sources, domains

@app.route("/news", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		sources, domains = get_sources_and_domains()
		keyword = request.form["keyword"]
		related_news = newsapi.get_everything(q=keyword,
									sources=sources,
									domains=domains,
									language='en',
                                    category='business',
									sort_by='relevancy')
		no_of_articles = related_news['totalResults']
		if no_of_articles > 100:
			no_of_articles = 100
		all_articles = newsapi.get_everything(q=keyword,
									sources=sources,
									domains=domains,
									language='en',
                                    category='business',
									sort_by='relevancy',
									page_size = no_of_articles)['articles']
		return render_template("news.html", all_articles = all_articles,
							keyword=keyword)
	else:
		top_headlines = newsapi.get_top_headlines(country="us", language="en", category="business")
		total_results = top_headlines['totalResults']
		if total_results > 100:
			total_results = 100
		all_headlines = newsapi.get_top_headlines(country="us",
													language="en",
                                                    category="business",
													page_size=total_results)['articles']
		return render_template("news.html", all_headlines = all_headlines)
	return render_template("news.html")
