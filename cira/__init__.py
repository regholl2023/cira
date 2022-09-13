"""
Cira

A simpler libray for alpaca-trade-api from Alpaca Markets.
"""

import alpaca_trade_api as tradeapi
import alpaca

from . import auth
from . import config
from . import util
from . import logging
from .exchange import Exchange
from .portfolio import Portfolio
from . import assets
__version__ = "2.3.0"
__author__ = "Axel Gard"
__credits__ = "alpaca.markets"
