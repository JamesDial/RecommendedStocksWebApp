import datetime

from werkzeug.security import check_password_hash

from app import db
from app.models import Investor, Stock, Crypto, Watchlist, stocks_crypto_by_risk




def create_database():
    """
    This function creates the database with all the tables.
    :return: none
    """

    db.create_all()
    db.session.commit()


def addNewInvestor(firstName, lastName, userEmail, password):
    """
    This function adds a new investor to the database. It also adds his email to all table by calling the following
    functions: addRiskLevel, addStocks, addCrypto, and addWatchlist.
    :param firstName: User first name
    :param lastName:  User last name
    :param userEmail: User email
    :param password: User password
    :return: none
    """

    newInvestor = Investor(firstName, lastName, userEmail, password)
    db.session.add(newInvestor)
    db.session.commit()


def addStocks(name, symbol, price):
    """
    This function add a new investor to the stocks table.
    :param userName: User email
    :return: none
    """
    newStocks = Stock(name, symbol, price)
    db.session.add(newStocks)
    db.session.commit()


def deleteStocks(name):
    """
    This function deletes the recommended stocks base off risk level
    :param userEmail: user email
    :return: none
    """
    Stock.query.filter_by(name=name).delete()
    db.session.commit()


def addCrypto(name, symbol, price):
    """
    This function add a new investor to the crypto table.
    :param userName: User email
    :return: none
    """
    newCrypto = Crypto(name, symbol, price)
    db.session.add(newCrypto)
    db.session.commit()


def deleteCrypto(name):
    """
    This function deletes the recommended crypto base off risk level
    :param userEmail: user email
    :return: none
    """
    Crypto.query.filter_by(name=name).delete()
    db.session.commit()


def addWatchlist(userEmail, name, symbol, price, type):
    """
    This function add an investor favorite stock or crypto to the watchlist.
    :param userEmail: user email
    :param name: name of stock or crypto
    :param symbol: symbol of stock or crypto
    :param price: price of stock or crypto
    :param type: type (stock or crypto)
    :return: none
    """
    newWatchlist = Watchlist(userEmail, name, symbol, price, type)
    db.session.add(newWatchlist)
    db.session.flush()
    db.session.commit()


def deleteWatchlist(userEmail, name):
    """
    This function removes a stock or crypto from the watchlist.
    :param userEmail: user email
    :param name: name of stock or crypto to be removed
    :return: none
    """
    Watchlist.query.filter_by(userEmail=userEmail, name=name).delete()
    db.session.commit()


def updatedRiskLevel(userEmail: str, risk):
    """
    This function updates the current risk level with a new risk level after the investors take his survey.
    :param userName: User email
    :param risk: new risk level
    :return: none
    """
    Investor.query.filter_by(userEmail=userEmail).update(dict(riskLevel=risk))
    db.session.commit()


def checkForInvestor(userEmail: str, password: str) -> Investor:
    """
    This function check to see if an investor email and password are in the database.
    :param userName: User email
    :param password: the user's password in plaintext
    :return: the Investor object representing the user if email and password match, None otherwise
    """
    exists = db.session.query(db.exists().where(Investor.userEmail == userEmail)).scalar()

    if exists:
        user = Investor.query.filter_by(userEmail=userEmail).first()
        if check_password_hash(user.password, password):
            return user

    else:
        exists = False





# def checkInvestorPassword(userEmail, password) -> bool:
#     """
#     This function check to see if the investors password matches what is in the database.
#     :param userEmail: User email
#     :param password: User password in plaintext
#     :return: True if the password matches the userEmail's, False otherwise
#     """
#
#     user = Investor.query.filter_by(userEmail=userEmail).first()
#     # TODO: What are you going to do if there is no Investor with the provided email?
#
#     return check_password_hash(user.password, password)


def reset():
    """
    This method is triggered by visiting the /resetdb route from the main page.
    """

    # Delete all data from all tables.
    Investor.query.delete()
    Stock.query.delete()
    Crypto.query.delete()
    Watchlist.query.delete()
    stocks_crypto_by_risk.query.delete()

    # Insert some user data
    u = Investor(firstName='Kris',
                 lastName='Valdez',
                 userEmail='kris@example.com',
                 password='1234pass')
    db.session.add(u)

    u = Investor(firstName='Mike',
                 lastName='McKinnon',
                 userEmail='mike@example.com',
                 password='word5678')

    db.session.add(u)

    u = Investor(firstName='James',
                 lastName='Dial',
                 userEmail='james@example.com',
                 password='marv8902')
    db.session.add(u)

    s = stocks_crypto_by_risk(name='Ford',
                              symbol='F',
                              price=15.34,
                              type='Stock',
                              risk='Medium')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Xpeng Inc - ADR',
                              symbol='XPEV',
                              price=26.82,
                              type='Stock',
                              risk='Medium')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Exxon Mobil Corp',
                              symbol='XOM',
                              price=85.66,
                              type='Stock',
                              risk='Medium')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Newegg Commerce Inc',
                              symbol='NEGG',
                              price=6.86,
                              type='Stock',
                              risk='Medium')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Coinbase Global Inc',
                              symbol='COIN',
                              price=153.32,
                              type='Stock',
                              risk='Medium')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Apple Inc',
                              symbol='AAPL',
                              price=168.60,
                              type='Stock',
                              risk='Low')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Meta Platforms Inc',
                              symbol='FB',
                              price=215.50,
                              type='Stock',
                              risk='Low')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Microsoft Corporation',
                              symbol='MSFT',
                              price=284.16,
                              type='Stock',
                              risk='Low')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Amazon.com, Inc',
                              symbol='AMZN',
                              price=3030.59,
                              type='Stock',
                              risk='Low')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Tesla Inc',
                              symbol='TSLA',
                              price=997.12,
                              type='Stock',
                              risk='Low')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Baozun Inc',
                              symbol='BZUN',
                              price=8.40,
                              type='Stock',
                              risk='High')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Electrameccanica Vehicles Corp',
                              symbol='SOLO',
                              price=1.93,
                              type='Stock',
                              risk='High')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Astra Space Inc',
                              symbol='ASTR',
                              price=3.78,
                              type='Stock',
                              risk='High')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Clover Health Investments Corp',
                              symbol='CLOV',
                              price=3.14,
                              type='Stock',
                              risk='High')

    db.session.add(s)

    s = stocks_crypto_by_risk(name='Sundial Growers Inc',
                              symbol='SNDL',
                              price=0.57,
                              type='Stock',
                              risk='High')

    db.session.add(s)

    c = stocks_crypto_by_risk(name='Bitcoin USD',
                              symbol='BTC-USD',
                              price=40877.39,
                              type='Crypto',
                              risk='High')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Dogecoin USD',
                              symbol='DOGE-USD',
                              price=0.14,
                              type='Crypto',
                              risk='High')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='SHIBA INU USD',
                              symbol='SHIB-USD',
                              price=0.000027,
                              type='Crypto',
                              risk='High')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='eCash Price',
                              symbol='XEC',
                              price=0.9123,
                              type='Crypto',
                              risk='High')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='EOS Price',
                              symbol='EOS-USD',
                              price=2.56,
                              type='Crypto',
                              risk='High')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Tether',
                              symbol='USDT',
                              price=1.0003,
                              type='Crypto',
                              risk='Low')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='USD Coin',
                              symbol='USDC',
                              price=1.0001,
                              type='Crypto',
                              risk='Low')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Celo Dollar',
                              symbol='CUSDT-USD',
                              price=1.00,
                              type='Crypto',
                              risk='Low')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Dai price',
                              symbol='DAI-USD',
                              price=1.00,
                              type='Crypto',
                              risk='Low')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Cronos',
                              symbol='CRO-USD',
                              price=0.4223,
                              type='Crypto',
                              risk='Low')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Cardano USD',
                              symbol='ADA-USD',
                              price=0.977766,
                              type='Crypto',
                              risk='Medium')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Avalanche USD',
                              symbol='AVAX-USD',
                              price=80.08,
                              type='Crypto',
                              risk='Medium')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Ethereum USD',
                              symbol='ETH-USD',
                              price=3106.34,
                              type='Crypto',
                              risk='Medium')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Solana USD',
                              symbol='SOL-USD',
                              price=105.62,
                              type='Crypto',
                              risk='Medium')

    db.session.add(c)

    c = stocks_crypto_by_risk(name='Polkadot USD',
                              symbol='DOT-USD',
                              price=18.20,
                              type='Crypto',
                              risk='Medium')

    db.session.add(c)

    db.session.commit()

    addStocks(name='Baozun Inc', symbol='BZUN', price=7.73)
    addStocks(name='Electranmeccanica Vehicles Corp', symbol='SOLO', price=1.95)
    addStocks(name='Astra Space Inc', symbol='ASTR', price=3.64)
    addStocks(name='Clover Health Investments Corp', symbol='CLOV', price=3.01)
    addStocks(name='Sundial Growers Inc', symbol='SNDL', price=0.54)
    addStocks(name='Apple Inc', symbol='AAPL', price=167.26)
    addStocks(name='Meta Platforms Inc', symbol='FB', price=207.95)
    addStocks(name='Microsoft Corporation', symbol='MSFT', price=286.30)
    addStocks(name='Amazon.com, Inc', symbol='AMZN', price=3093.36)
    addStocks(name='Tesla Inc', symbol='TSLA', price=1008.48)
    addStocks(name='Alphabet Inc Class C', symbol='GOOG', price=2598.50)
    addStocks(name='Ford Motor Company', symbol='F', price=16.17)
    addStocks(name='Xpeng Inc - ADR', symbol='XPEV', price=25.71)
    addStocks(name='Exxon Mobil Corp', symbol='XOM', price=87.60)
    addStocks(name='Newegg Commerce Inc', symbol='NEGG', price=6.24)
    addStocks(name='Coinbase Global Inc', symbol='COIN', price=146.39)
    addStocks(name='JPMorgan Chase & Co', symbol='JPM', price=132.25)
    addStocks(name='Wells Fargo & Co', symbol='WFC', price=48.55)
    addStocks(name='Bank of America Corp', symbol='BAC', price=39.99)
    addStocks(name='HSBC Holding plc', symbol='HSBC', price=35.14)
    addStocks(name='Citigroup Inc', symbol='C', price=53.59)
    addStocks(name='Markel Corporation', symbol='MKL', price=1480.67)
    addStocks(name='White Mountains Insurance Group Ltd', symbol='WTM', price=1074.41)
    addStocks(name='Alleghany Corporation', symbol='Y', price=839.44)
    addStocks(name='Equinix Inc', symbol='EQIX', price=762.29)
    addStocks(name='BlackRock Inc', symbol='BLK', price=706.75)
    addStocks(name='First Citizens BancShares Inc', symbol='FCNCA', price=663.14)
    addStocks(name='AMERCO', symbol='UHAL', price=567.25)
    addStocks(name='Credit Acceptance Corp', symbol='CACC', price=621.46)
    addStocks(name='SCB Financial Group', symbol='SIVB', price=528.95)
    addStocks(name='Mastercard Inc', symbol='MA', price=370.60)
    addStocks(name='Applied Optoelectronics Inc', symbol='AAOI', price=2.99)
    addStocks(name='Axcelis Technologies Inc', symbol='ACLS', price=59.71)
    addStocks(name='Advanced Micro Devices Inc', symbol='AMD', price=94.84)
    addStocks(name='Ambarella Inc', symbol='AMBA', price=89.31)
    addStocks(name='Avid Technology Inc', symbol='AVID', price=36.01)
    addStocks(name='Azenta Inc', symbol='AZTA', price=83.35)
    addStocks(name='Canon Inc', symbol='CAJ', price=24.71)
    addStocks(name='Dell Technologies Inc', symbol='DELL', price=49.46)
    addStocks(name='Digital Ally Inc', symbol='DGLY', price=1.12)
    addStocks(name='Alphabet Inc Class A', symbol='GOOGL', price=2566.20)
    addStocks(name='BlackBerry Ltd', symbol='BB', price=6.50)
    addStocks(name='Oracle Corporation', symbol='ORCL', price=81.31)
    addStocks(name='Intel Corporation', symbol='INTC', price=48.06)
    addStocks(name='Amplify Energy Corp', symbol='AMPY', price=7.22)
    addStocks(name='Alpha Metallurgical Resources Inc', symbol='AMR', price=153.94)
    addStocks(name='APA Corp', symbol='APA', price=44.38)
    addStocks(name='Antero Resources Corp', symbol='AR', price=35.70)
    addStocks(name='Arch Resources Inc', symbol='ARCH', price=163.20)
    addStocks(name='American Resources Corp', symbol='AREC', price=2.36)
    addStocks(name='Pioneer Natural Resources Co', symbol='PXD', price=250.94)
    addStocks(name='Acadia Healthcare Company Inc', symbol='ACHC', price=76.03)
    addStocks(name='Addus Homecare Corporation', symbol='ADUS', price=91.88)
    addStocks(name='Agilon Health Inc', symbol='AGL', price=22.62)
    addStocks(name='Aesthetic Medical International HldngsGL', symbol='AIH', price=1.47)
    addStocks(name='Akumin Inc', symbol='AKU', price=1.41)
    addStocks(name='UnitedHealth Group Inc', symbol='UNH', price=543.22)
    addStocks(name='Chemed Corporation', symbol='CHE', price=505.80)
    addStocks(name='Humana Inc', symbol='HUM', price=461.68)
    addStocks(name='Molina Healthcare Inc', symbol='MOH', price=340.84)
    addStocks(name='Cellnet Group Limited', symbol='CLT', price=0.037)
    addStocks(name='Cigna Corp', symbol='CI', price=268.19)
    addStocks(name='HCA HealthCare', symbol='HCA', price=273.55)
    addStocks(name='Iqvia Holdings Inc', symbol='IQV', price=243.35)
    addStocks(name='LHC Group Inc', symbol='LHCG', price=167.36)
    addStocks(name='Amedisys Inc', symbol='AMED', price=151.99)
    addStocks(name='Universal Health Services Inc Class B', symbol='UHS', price=156.16)
    addStocks(name='Quest Diagnostics Inc', symbol='DGX', price=138.57)
    addStocks(name='Alignment Healthcare Inc', symbol='ALHC', price=10.71)
    addStocks(name='ALIOR BANK SA', symbol='ALR', price=43.66)
    addStocks(name='Ameren Corp', symbol='AEE', price=98.04)
    addStocks(name='American Electric Power Company Inc', symbol='AEP', price=103.71)
    addStocks(name='AES Corp', symbol='AES', price=24.97)
    addStocks(name='AES Units', symbol='AESC', price=98.65)
    addStocks(name='Avangrid Inc', symbol='AGR', price=4.49)
    addStocks(name='ALLETE Inc', symbol='ALE', price=64.65)
    addStocks(name='ALtus Power Inc', symbol='AMPS', price=6.43)
    addStocks(name='American Airlines Group Inc', symbol='AAL', price=19.70)
    addStocks(name='Atlas Air Worldwide Holdings Inc', symbol='AAWW', price=70.39)
    addStocks(name='Air T Inc', symbol='AIRT', price=18.00)
    addStocks(name='Alask Air Group Inc', symbol='ALK', price=58.65)
    addStocks(name='ArcBest Corp', symbol='ARCB', price=75.09)
    addStocks(name='Ardmore Shipping Corp', symbol='ASC', price=5.38)
    addStocks(name='Grupo Aeroportuario dl Srst SAB CV', symbol='ASR', price=207.32)
    addStocks(name='Alibaba Group Holding Ltd - ADR', symbol='BABA', price=90.08)
    addStocks(name='AT&T Inc', symbol='T', price=19.52)
    addStocks(name='Airbnb Inc', symbol='ABNB', price=166.00)
    addStocks(name='AMC Entertainment Holdings Inc', symbol='AMC', price=17.88)
    addStocks(name='Ark Restaurants Corp', symbol='ARKR', price=18.68)
    addStocks(name='American Public Education Inc', symbol='APEI', price=22.17)
    addStocks(name='Aramark', symbol='ARMK', price=38.27)
    addStocks(name='Arcos Dorados Holdings Inc', symbol='ARCO', price=7.94)
    addStocks(name='Booking Holdings Inc', symbol='BKNG', price=2282.89)
    addStocks(name='Chipotle Mexican Grill Inc', symbol='CMG', price=1625.80)
    addStocks(name='Cable One Inc', symbol='CABO', price=1421.02)
    addStocks(name='Walmart Inc', symbol='WMT', price=159.85)
    addStocks(name='Visa Inc', symbol='V', price=219.12)
    addStocks(name='Berkshine Hathway Inc Class A', symbol='BRK.A', price=523995.60)
    addStocks(name='Broadcom Inc', symbol='AVGO', price=598.88)
    addCrypto(name='Aave', symbol='AAVE', price=194.14)
    addCrypto(name='Algorand', symbol='ALGO', price=0.7498)
    addCrypto(name='Amp', symbol='AMP', price=0.0222)
    addCrypto(name='Apecoin', symbol='APE', price=15.95)
    addCrypto(name='Arweave', symbol='AR', price=31.17)
    addCrypto(name='Avalanche', symbol='AVAX', price=80.56)
    addCrypto(name='Axie Infinity', symbol='AXS', price=47.35)
    addCrypto(name='Basic Attention Token', symbol='BAT', price=0.76618)
    addCrypto(name='BNB', symbol='BNB', price=430.44)
    addCrypto(name='Binance USD', symbol='BUSD', price=0.999)
    addCrypto(name='Bitcoin', symbol='BTC', price=41571.00)
    addCrypto(name='Bitcoin Cash', symbol='BCH', price=337.61)
    addCrypto(name='BitDAO', symbol='BIT', price=1.26)
    addCrypto(name='BitTorrent', symbol='BTTOLD', price=0.001921)
    addCrypto(name='Stacks', symbol='STX', price=1.18)
    addCrypto(name='Cardano', symbol='ADA', price=0.94)
    addCrypto(name='Compound Dai', symbol='CDAI', price=0.0219)
    addCrypto(name='Celo', symbol='CELO', price=3.33)
    addCrypto(name='Celsius', symbol='CEL', price=2.27)
    addCrypto(name='Chainlink', symbol='LINK', price=14.28)
    addCrypto(name='Chiliz', symbol='CHZ', price=0.224)
    addCrypto(name='cETH', symbol='CETH', price=60.98)
    addCrypto(name='Compound USD', symbol='CUSDC', price=0.0225)
    addCrypto(name='Convex Finance', symbol='CVX', price=29.16)
    addCrypto(name='Cosmos', symbol='ATOM', price=24.77)
    addCrypto(name='Cronos', symbol='CRO', price=0.423)
    addCrypto(name='Dai', symbol='DAI', price=0.999692)
    addCrypto(name='Dash', symbol='DASH', price=108.45)
    addCrypto(name='Decentraland', symbol='MANA', price=2.11)
    addCrypto(name='DeFiChain', symbol='DFI', price=4.42)
    addCrypto(name='Dogecoin', symbol='DOGE', price=0.14)
    addCrypto(name='eCash', symbol='XEC', price=0.9123)
    addCrypto(name='Elrond', symbol='EGLD', price=162.70)
    addCrypto(name='Enjin Coin', symbol='ENJ', price=1.51)
    addCrypto(name='EOS', symbol='EOS', price=2.78)
    addCrypto(name='Ethereum', symbol='ETH', price=3089.85)
    addCrypto(name='Ethereum Classic', symbol='ETC', price=36.62)
    addCrypto(name='Fantom', symbol='FTM', price=1.18)
    addCrypto(name='Filecoin', symbol='FIL', price=19.82)
    addCrypto(name='Flow', symbol='FLOW', price=5.754)
    addCrypto(name='Frax', symbol='FRAX', price=1.00)
    addCrypto(name='Frax Share', symbol='FXS', price=36.93)
    addCrypto(name='FTX Token', symbol='FTT', price=42.72)
    addCrypto(name='Gala', symbol='GALA', price=0.1969)
    addCrypto(name='Harmony', symbol='ONE', price=0.126849)
    addCrypto(name='PancakeSwap', symbol='CAKE', price=9.07)
    addCrypto(name='Polkadot', symbol='DOT', price=19.06)
    addCrypto(name='Shiba Inu', symbol='SHIB', price=.000025)
    addCrypto(name='XRP', symbol='XRP', price=0.75531)
    addCrypto(name='Solana', symbol='SOL', price=107.08)
    addCrypto(name='Stellar', symbol='XLM', price=0.201903)
    addCrypto(name='Tezos', symbol='XTZ', price=3.10)
    addCrypto(name='The Sandbox', symbol='SAND', price=2.85)
    addCrypto(name='USD Coin', symbol='USDC', price=0.999988)
    addCrypto(name='VeChain', symbol='VET', price=0.061267)
    addCrypto(name='Tether', symbol='USDT', price=1.00)
    db.session.commit()




