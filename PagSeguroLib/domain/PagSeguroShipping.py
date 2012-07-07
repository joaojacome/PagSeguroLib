from PagSeguroLib.domain.PagSeguroAddress import PagSeguroAddress
from PagSeguroLib.domain.PagSeguroShippingType import PagSeguroShippingType

class PagSeguroShipping:

    address = None
    _type = None
    cost = None

    def __init__(self, data = None): 
        if data:
            if 'address' in data and isinstance(data['address'], PagSeguroAddress):  
                self.address = data['address']
            if 'type' in data and isinstance(data['type'], PagSeguroShippingType):
                self._type = data['type']
            if 'cost' in data:  
                self.cost = data['cost']
                
    def setAddress(self, address):
        self.address = address
        
    def getAddress(self):
        return self.address
     
    def setType(self, _type):
        self._type = _type
        
    def getType(self):
        return self._type
     
    def setCost(self,cost):
        self.cost = cost
        
    def getCost(self):
        return self.cost