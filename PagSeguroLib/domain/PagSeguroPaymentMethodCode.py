class PagSeguroPaymentMethodCode:
    
    codeList = {
        'VISA_CREDIT_CARD': 101,
        'MASTERCARD_CREDIT_CARD': 102,
        'AMEX_CREDIT_CARD': 103,
        'DINERS_CREDIT_CARD': 104,
        'HIPERCARD_CREDIT_CARD': 105,
        'AURA_CREDIT_CARD': 106,
        'ELO_CREDIT_CARD': 107,
        'BRADESCO_BOLETO': 201,
        'SANTANDER_BOLETO': 202,
        'BRADESCO_ONLINE_TRANSFER': 301,
        'ITAU_ONLINE_TRANSFER': 302,
        'UNIBANCO_ONLINE_TRANSFER': 303,
        'BANCO_BRASIL_ONLINE_TRANSFER': 304,
        'REAL_ONLINE_TRANSFER': 305,
        'BANRISUL_ONLINE_TRANSFER': 306,
        'PS_BALANCE': 401,
        'OI_PAGGO': 501
    }
    value = None
    
    def __init__(self, value = None):
        if value:
            self.value = value
            
    def setValue(self, value):
        self.value = value
        
    def setByType(self, _type):
        if _type in self.codeList:
            self.value = self.codeList[_type]
        else:
            raise NameError("undefined index %s" % _type)
    
    def getValue(self):
        return self.value
    
    def getTypeFromValue(self, value = None):
        if value == None:
            value = self.value
        for i in self.codeList:
            if self.codeList[i] == int(value):
                return i