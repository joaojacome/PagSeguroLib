from datetime import datetime
from time import time
from decimal import Decimal
class PagSeguroHelper:
    @classmethod
    def formatDate(cls, date):
        _format = "%Y-%m-%d\T%H:%M:%S"
        if isinstance(date, datetime):
            d = date.strftime(_format)
        elif isinstance(date, int):
            #time.localtime(date)
            d = datetime.strptime(time.localtime(date), _format)
        else:
            d = date
        return d
    
    @classmethod
    def decimalFormat(cls, number):
        TWOPLACES = Decimal(10) ** -2
        return Decimal(number).quantize(TWOPLACES)