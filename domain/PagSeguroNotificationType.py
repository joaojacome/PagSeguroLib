class PagSeguroNotificationType:
    typeList = {
        'TRANSACTION': 'transaction'
    }
    value = None
    
    def __init__(self, value = None):
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
            if self.typeList[i] == value:
                return i