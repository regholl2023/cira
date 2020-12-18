import alpaca_trade_api as tradeapi
from . import config 
from . import alpaca
from . import util

class Portfolio:
    def __init__(self):
        self.equity = 0
        self._list_orders = []
        self._owned_stocks = []
        

    @property
    def orders(self):
        """ returns a list of all open orders with all diffult args """
        self._list_orders = alpaca.api().list_orders()
        return self._list_orders


    @property
    def get_position(): # PREV: get_position
        """ create a list of all owned position """
        portfolio = alpaca.api().list_positions()
        portfolio_lst = []
        for position in portfolio:
            position_dict = util.reformat_position(position)
            position_dict['symbol'] = position.symbol
            portfolio_lst.append(position_dict)
        return portfolio_lst


    
    def owned_stock_qty(self, stock): # maby shuld be in stock.Stock 
        """ returns quantity of owned of a stock Stock (obj) """
        position = util.reformat_position(stock.position)
        return position['qty']


    @property
    def owned_stocks(self):
        """ returns a list of owned stocks """
        lst = get_position()
        self._owned_stocks = []
        for dict_ in lst:
            self._owned_stocks.append(dict_['symbol'])
        return self._owned_stocks


    @property
    def sell_list(self, lst):
        """ takes a list of symbols (str) and sells all stocks in that list """
        for stock in lst:
            qty = self.owned_stock_qty(stock)
            #if not stock.symbol == 'GOOGL':  # BUG: fix, google has problem selling! 
            stock.sell(qty)
    
    