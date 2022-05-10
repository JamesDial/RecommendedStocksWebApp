from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from app import db, login


@login.user_loader
def load_user(email):
    return Investor.query.get(email)


class Investor(UserMixin, db.Model):
    """
    This class creates the investor table of the database.
    """

    __tablename__ = "Investor"
    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    userEmail = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    riskLevel = db.Column(db.String, nullable=True, default='NULL')


    def __init__(self, firstName, lastName, userEmail, password):
        self.firstName = firstName
        self.lastName = lastName
        self.userEmail = userEmail
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "FirstName:{}\tLastName:{}\tUserEmail:{}\tPassword:{}" \
            .format(self.firstName, self.lastName, self.userEmail, self.password)


class Stock(db.Model):
    """
    This class creates the stocks table of the database.
    """
    __tablename__ = "Stock"
    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    Name = db.Column(db.String, nullable=True)
    Symbol = db.Column(db.String, nullable=True)
    Price = db.Column(db.Float, nullable=True)

    def __init__(self, Name, Symbol, Price):
        self.Name = Name
        self.Symbol = Symbol
        self.Price = Price

    def __repr__(self):
        return "Name:{}\tSymbol:{}\tPrice:{}\t".format(self.Name, self.Symbol, self.Price)


class Crypto(db.Model):
    """
    This class creates the crypto table of the database.
    """
    __tablename__ = "Crypto"
    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    Name = db.Column(db.String, nullable=True)
    Symbol = db.Column(db.String, nullable=True)
    Price = db.Column(db.Float, nullable=True)

    def __init__(self, Name, Symbol, Price):
        self.Name = Name
        self.Symbol = Symbol
        self.Price = Price

    def __repr__(self):
        return "Name:{}\tSymbol:{}\tPrice:{}".format(self.Name, self.Symbol, self.Price)



class Watchlist(db.Model):
    """
    This class creates the watchlist table of the database.
    """
    __tablename__ = "Watchlist"
    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    userEmail = db.Column(db.String, db.ForeignKey('Investor.userEmail'))
    name = db.Column(db.String, nullable=True)
    symbol = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=True)
    type = db.Column(db.String, nullable=True)

    def __init__(self, Email, name, symbol, price, type):
        self.userEmail = Email
        self.name = name
        self.symbol = symbol
        self.price = price
        self.type = type

    def __repr__(self):
        return "userEmail:{}\tName:{}\tSymbol:{}\tPrice:{}\tType:{}".format(self.userEmail, self.name, self.symbol,
                                                                            self.price, self.type)


class stocks_crypto_by_risk(db.Model):
    """
       This class creates the watchlist table of the database.
    """
    __tablename__ = "Stock and Crypto by risk"
    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String, nullable=True)
    symbol = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=True)
    type = db.Column(db.String, nullable=True)
    risk = db.Column(db.String, nullable=True)

    def __init__(self, name, symbol, price, type, risk):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.type = type
        self.risk = risk

    def __repr__(self):
        return "Name:{}\tSymbol:{}\tPrice:{}\tType:{}\tRisk:{}".format(self.name, self.symbol, self.price, self.type,
                                                                       self.risk)
