from datetime import datetime
from time import time
class PagSeguroHelper:
    @classmethod
    def formatDate(cls, date):
        _format = "%Y-%m-%d\T%H:%M:%S"
        if isinstance(date, datetime):
            d = date.strftime(_format)
        elif isinstance(date, int):
            d = datetime.strptime(time.localtime(date), _format)
        else:
            d = date
        return d
    
    @classmethod
    def decimalFormat(cls, number):
        return "%.2f" % number
