class PagSeguroAddress:
    postalCode = None
    street = None
    number = None
    complement = None
    district = None
    city = None
    state = None
    country = None
    
    def __init__(self, data = None):
        if 'postalCode' in data:
            self.postalCode = data['postalCode']
        if 'street' in data:
            self.street = data['street']
        if 'number' in data:
            self.number = data['number']
        if 'complement' in data:
            self.complement = data['complement']
        if 'district' in data:
            self.district = data['district']
        if 'city' in data:
            self.city = data['city']
        if 'state' in data:
            self.state = data['state']
        if 'country' in data:
            self.country = data['country']
            
    def getStreet(self):
        return self.street
    
    def getNumber(self):
        return self.number
    
    def getComplement(self):
        return self.complement
    
    def getDistrict(self):
        return self.district
    
    def getState(self):
        return self.state
    
    def getPostalCode(self):
        return self.postalCode
    
    def getCountry(self):
        return self.country
    
    def setStreet(self, street):
        self.street = street
        
    def setNumber(self, number):
        self.number = number
        
    def setComplement(self, complement):
        self.complement = complement
        
    def setDistrict(self, district):
        self.district = district
    
    def setState(self, state):
        self.state = state
        
    def setPostalCode(self, postalCode):
        self.postalCode = postalCode
        
    def setCountry(self, country):
        self.country = country