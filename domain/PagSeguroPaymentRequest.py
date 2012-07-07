from PagSeguroLib.domain.PagSeguroSender import PagSeguroSender
from PagSeguroLib.domain.PagSeguroPhone import PagSeguroPhone
from PagSeguroLib.domain.PagSeguroItem import PagSeguroItem
from PagSeguroLib.service.PagSeguroPaymentService import PagSeguroPaymentService
from PagSeguroLib.domain.PagSeguroShipping import PagSeguroShipping
from PagSeguroLib.domain.PagSeguroShippingType import PagSeguroShippingType
from PagSeguroLib.domain.PagSeguroAddress import PagSeguroAddress
class PagSeguroPaymentRequest:
    sender = None
    currency = None
    items = None
    itemsCount = 0
    redirectURL = None
    extraAmount = None
    reference = None
    shipping = None
    maxAge = None
    maxUses = None
    
    def getSender(self):
        return self.sender
    
    def setSender(self, name, email = None, areaCode = None, number = None):
        param = name
        if isinstance(param, (list, tuple)):
            self.sender = PagSeguroSender(param)
        else:
            sender = PagSeguroSender()
            sender.setName(param)
            sender.setEmail(email)
            sender.setPhone(PagSeguroPhone(areaCode, number))
            self.sender = sender
            
    def setSenderName(self, senderName):
        if self.sender == None:
            self.sender = PagSeguroSender()
        self.sender.setName(senderName)
        
    def setSenderEmail(self, senderEmail):
        if self.sender == None:
            self.sender = PagSeguroSender()
        self.sender.setEmail(senderEmail)
        
    def setSenderPhone(self, areaCode, number = None):
        param = areaCode
        if self.sender == None:
            self.sender = PagSeguroSender()
        if isinstance(param, PagSeguroPhone):
            self.sender.setPhone(param)
        else:
            self.sender.setPhone(PagSeguroPhone(param, number))
    
    def getCurrency(self):
        return self.currency
    
    def setCurrency(self, currency):
        self.currency = currency    
        
    def getItems(self):
        return self.items
    
    def setItems(self, items):
        if isinstance(items, (list, tuple)):
            i = {}
            for x, v in items:
                if isinstance(v, PagSeguroItem):
                    i[x] = v
                elif isinstance(v, (list, tuple)):
                    i[x] = PagSeguroItem(v)
            self.items = i
            
    def addItem(self, _id, description = None, quantity = None, amount = None, weight = None, shippingCost = None):
        param = _id
        if self.items == None:
            self.items = {}
        if isinstance(param, (list, tuple)):
            self.items[self.itemsCount] = PagSeguroItem(param)
            self.itemsCount = self.itemsCount + 1
        elif isinstance(param, PagSeguroItem):
            self.items[self.itemsCount] = param
            self.itemsCount = self.itemsCount + 1
        else:
            item = PagSeguroItem()
            item.setId(param)
            item.setDescription(description)
            item.setQuantity(quantity)
            item.setAmount(amount)
            item.setWeight(weight)
            item.setShippingCost(shippingCost)
            self.items[self.itemsCount] = item
            self.itemsCount = self.itemsCount + 1
            
    def getRedirectURL(self):
        return self.redirectURL
    
    def setRedirectURL(self, redirectURL):
        self.redirectURL = redirectURL
        
    def getExtraAmount(self):
        return self.extraAmount
    
    def setExtraAmount(self, extraAmount):
        self.extraAmount = extraAmount
        
    def getReference(self):
        return self.reference
    
    def setReference(self, reference):
        self.reference = reference
    
    def getShipping(self):
        return self.shipping
    
    def setShipping(self, address, _type=None):
        param = address
        if isinstance(param,PagSeguroShipping):
            self.shipping = param
        else:
            shipping = PagSeguroShipping()
            if isinstance(param, (list, tuple)):
                shipping.setAddress(PagSeguroAddress(param))
            elif isinstance(param, PagSeguroAddress):
                shipping.setAddress(param)
            if type:
                if isinstance(_type, PagSeguroShippingType):
                    shipping.setType(_type)
                else:
                    shipping.setType(PagSeguroShippingType(_type))
            self.shipping = shipping
            
    def setShippingAddress(self, postalCode = None, street = None, number = None, complement = None, district = None, city = None, state = None, country = None):
        param = postalCode
        if self.shipping == None:
            self.shipping = PagSeguroShipping()
        if isinstance(param, (list, tuple)):
            self.shipping.setAddress(PagSeguroAddress(param))
        elif isinstance(param,PagSeguroAddress):
            self.shipping.setAddress(param)
        else:
            address = PagSeguroAddress()
            address.setPostalCode(postalCode)
            address.setStreet(street)
            address.setNumber(number)
            address.setComplement(complement)
            address.setDistrict(district)
            address.setCity(city)
            address.setState(state)
            address.setCountry(country)
            self.shipping.setAddress(address)
    
    def setShippingType(self, _type):
        param = _type
        if self.shipping == None:
            self.shipping = PagSeguroShipping()
        if isinstance(param, PagSeguroShippingType):
            self.shipping.setType(param)
        else:
            self.shipping.setType(PagSeguroShippingType(param))
    
    def getMaxAge(self):
        return self.maxAge
    
    def setMaxAge(self, maxAge):
        self.maxAge = maxAge
        
    def getMaxUses(self):
        return self.maxUses
    
    def setMaxUses(self, maxUses):
        self.maxUses = maxUses
    
    def register(self, credentials):
        #TODO VERIFY INSTANCE CREDENTIALS
        return PagSeguroPaymentService.createCheckoutRequest(credentials, self)
    
    def __unicode__(self):
        email = None
        if self.sender and self.sender.getEmail():
            email = self.sender.getEmail()
        return "PagSeguroPaymentRequest(Reference=%s,     SenderEmail=%s)" % (self.reference, email)