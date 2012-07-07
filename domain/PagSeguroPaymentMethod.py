from PagSeguroLib.domain.PagSeguroPaymentMethodType import PagSeguroPaymentMethodType
from PagSeguroLib.domain.PagSeguroPaymentMethodCode import PagSeguroPaymentMethodCode

class PagSeguroPaymentMethod:
    _type = None
    code = None
    
    def __init__(self, _type=None, code=None):
        if type:
            self.setType(_type)
        if code:
            self.setCode(code)
            
    def getType(self):
        return self.type
    
    def setType(self, _type):
        if isinstance(_type, PagSeguroPaymentMethodType):
            return self._type
        else:
            self._type = PagSeguroPaymentMethodType(_type)
            
    def getCode(self):
        return self.code
    
    def setCode(self, code):
        if isinstance(code, PagSeguroPaymentMethodCode):
            return self.code
        else:
            self.code = PagSeguroPaymentMethodCode(code)
        