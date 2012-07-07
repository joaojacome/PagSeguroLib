class PagSeguroTransactionType:
    
    typeList={
        'PAYMENT': 1,
        'TRANSFER': 2,
        'FUND_ADDITION': 3,
        'WITHDRAW': 4,
        'CHARGE': 5,
        'DONATION': 6,
        'BONUS': 7,
        'BONUS_REPASS': 8,
        'OPERATIONAL': 9,
        'POLITICAL_DONATION': 10
    }
    value = None
    
    def __init__(self, value=None):
        if value:
            self.value = value
        
    def setValue(self, value):
        self.value = value
        
    def setByType(self, _type):
        if _type in self.typeList:
            self.value = self.typeList[_type]
        else:
            raise NameError("undefined index %s" % _type)
        
    def getValue(self):
        return self.value
    
    def getTypeFromValue(self, value = None):
        if value == None:
            value = self.value
        for i in self.typeList:
            if self.typeList[i] == int(value):
                return i