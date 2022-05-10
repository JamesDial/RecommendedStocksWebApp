try:
    import os
    import ufi_database
    import datetime
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import select

    print('All Import Module(s) found')
    print()

except:
    print('Error: Module(s) not found')

class WatchList:
    '''
    Functions Needed:
    Add to stock list
    Add to crypto list
    Add to watch list

    Remove from stock list
    Remove from crypto list

    Return stock count
    Return crypto count

    Return stock list
    Return crypto list
    Return price of given stock
    Return price of given crypto
    '''

    def __init__(self):

        '''
        Dictionary name/price pair for Stock and Crypto '''

        self.stockList = {}
        self.cryptoList = {}

        self.stockCount = 0
        self.cryptoCount = 0

    def stockAdd(self, stock, price):
        '''
        Method to add the given stock to the current stock watch list
        Parameters: 2 a stock of type String and a price
        Returns: Success message or stock already exists
        '''

        print(f'Trying to add {stock} to the stock list....')

        if stock not in self.stockList:
            self.stockList[str(stock)] = round(price, 2)
            self.stockCount += 1
            print(f'Stock: {stock} with a price of ${price} successfully added to stock list')
            print()

        else:
            print(f'{stock} already in list')
            print()

    def cryptoAdd(self, crypto, price):
        '''
        Method to add crypto to current crypto watch list
        Paramters: 2 a crypto of stype String and a price
        Returns: Success message or crypto already exists
        '''

        print(f'Trying to add {crypto} to the crypto list....')

        if crypto not in self.cryptoList:
            self.cryptoList[str(crypto)] = round(price, 2)
            self.cryptoCount += 1
            print(f'Crypto: {crypto} with a price of ${price} successfully added to the crypto list')
            print()

        else:
            print(f'{crypto} already in the crypto list')
            print()

    def stockRemove(self, stock):
        '''
        Method to remove stock from current stock list
        Paramters: 1 a stock of type String
        Returns: Success message or stock not found
        '''

        print(f'Trying to remove {stock} from the stock list....')

        try:
            del self.stockList[str(stock)]
            self.stockCount -= 1
            print(f'{stock} successfully removed from the stock list')
            print()

        except:
            print(f'{stock} not found in list')
            print()

    def cryptoRemove(self, crypto):
        '''
        Method to remove crypto from current watch list
        Parameters: 1 a crypto of type String
        Returns: Success message or crypto not found
        '''

        print(f'Trying to remove {crypto} from the crypto list....')

        try:
            del self.cryptoList[str(crypto)]
            self.cryptoCount -= 1
            print(f'{crypto} successfully removed from the crypto list')
            print()

        except:
            print(f'{crypto} not found in list')
            print()

    def getStockCount(self):
        '''
        Method to return the length of the current stock watch list
        Paramters: None
        Returns: a count of the stock list of type int
        '''

        return self.stockCount

    def getCryptoCount(self):
        '''
        Method to return the length of current crypto watch list
        Parameters: None
        Returns: a count of the crypto list of type int
        '''

        return self.cryptoCount

    def getStockPrice(self, stock):
        '''
        :param stock: a name of a stock of type string
        :return: Return the price of a specified stock in the list
        '''

        print(f'Getting price of {stock}...')
        if stock in self.stockList:
            price = self.stockList[str(stock)]
            return f'Price per share of {stock} = ${price}'

        else:
            print(f'{stock} not found in the list')
            print()

    def getCryptoPrice(self, crypto):
        '''
        :param crypto: a name of a crypto of type string
        :return: Return the price of a specified crypto in the list
        '''

        print(f'Getting price of {crypto}...')
        if crypto in self.cryptoList:
            price = self.cryptoList[str(crypto)]
            return f'Price per share of {crypto} = ${price}'

        else:
            print(f'{crypto} not found in the list')
            print()

    def getStockList(self):
        return self.stockList

    def getCryptoList(self):
        return self.cryptoList