
class PagSeguroShippingType:
    typeList = {
        'PAC': 1,
        'SEDEX': 2,
        'NOT_SPECIFIED': 3
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
            if self.typeList[i] == int(value):
                return i
            
    @classmethod
    def getCodeByType(cls, _type):
        if _type in cls.typeList:
            return cls.typeList[_type]
        else:
            raise NameError("undefined index %s" % _type)
        
    @classmethod
    def createByType(cls, _type):
        shippingType = PagSeguroShippingType()
        shippingType.setByType(type)
        return shippingType