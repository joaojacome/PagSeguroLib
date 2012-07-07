class PagSeguroTransactionStatus:
    statusList = {
        'INITIATED': 0,
        'WAITING_PAYMENT': 1,
        'IN_ANALYSIS': 2,
        'PAID': 3,
        'AVAILABLE': 4,
        'IN_DISPUTE': 5,
        'REFUNDED': 6,
        'CANCELLED': 7
    }
    value = None
    
    def __init__(self, value = None):
        if value:
            self.value = value
    
    def setValue(self, value):
        self.value = value
        
    def setByType(self, _type):
        if _type in self.statusList:
            self.value = self.statusList[_type]
        else:
            raise NameError("undefined index %s" % _type)
        
    def getValue(self):
        return self.value
    
    def getTypeFromValue(self, value = None):
        if value == None:
            value = self.value
        for i in self.statusList:
            if self.statusList[i] == int(value):
                    return i