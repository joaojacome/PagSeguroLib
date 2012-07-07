from PagSeguroLib.domain.PagSeguroPhone import PagSeguroPhone
class PagSeguroSender:

    name = None
    email = None
    phone = None

    def __init__(self, data = None):
        if data:
            if 'name' in data:
                self.name = data['name']
                    
            if 'email' in data:
                self.email = data['email']
                    
            if data['phone'] and isinstance(data['phone'], PagSeguroPhone): 
                self.phone = data['phone']
                
            elif 'areacode' in data and 'number' in data: 
                phone =  PagSeguroPhone(data['areaCode'], data['number'])
                self.phone = phone

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def setPhone(self, areaCode, number = None):
        param = areaCode
        if isinstance(param, PagSeguroPhone):
            self.phone = param
        elif number: 
            phone = PagSeguroPhone()
            phone.setAreaCode(areaCode)
            phone.setNumber(number)
            self.phone = phone

    def getPhone(self): 
        return self.phone
    
    