class PagSeguroPhone:
    areaCode = None
    number = None
    
    def __init__(self, areaCode = None, number = None):
        if areaCode:
            self.areaCode = areaCode
        if number:
            self.number = number
    
    def getAreaCode(self):
        return self.areaCode
    
    def getNumber(self):
        return self.number
    
    def setAreaCode(self, areaCode):
        self.areaCode = areaCode
        
    def setNumber(self, number):
        self.number = number
