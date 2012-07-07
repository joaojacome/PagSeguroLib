class PagSeguroTransaction:
    
    date = None
    lastEventDate = None
    code = None
    reference = None
    _type = None
    status = None
    paymentMethod = None
    grossAmount = None
    discountAmount = None
    feeAmount = None
    netAmount = None
    extraAmount = None
    installmentCount = None
    items = None
    sender = None
    shipping = None
    
    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getLastEventDate(self):
        return self.lastEventDate

    def setLastEventDate(self, lastEventDate):
        self.lastEventDate = lastEventDate

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getReference(self):
        return self.reference

    def setReference(self, reference):
        self.reference = reference

    def getType(self):
        return self.type

    def setType(self, _type):
        self._type = _type

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getPaymentMethod(self):
        return self.paymentMethod

    def setPaymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod

    def getGrossAmount(self):
        return self.grossAmount

    def setGrossAmount(self, grossAmount):
        self.grossAmount = grossAmount

    def getDiscountAmount(self):
        return self.discountAmount

    def setDiscountAmount(self, discountAmount):
        self.discountAmount = discountAmount

    def getFeeAmount(self):
        return self.feeAmount

    def setFeeAmount(self, feeAmount):
        self.feeAmount = feeAmount

    def getNetAmount(self):
        return self.netAmount

    def setNetAmount(self, netAmount):
        self.netAmount = netAmount

    def getExtraAmount(self):
        return self.extraAmount

    def setExtraAmount(self, extraAmount):
        self.extraAmount = extraAmount

    def getInstallmentCount(self):
        return self.installmentCount

    def setInstallmentCount(self, installmentCount):
        self.installmentCount = installmentCount

    def getItems(self):
        return self.items

    def setItems(self, items):
        self.items = items
        
    def getItemCount(self):
        if self.items != None:
            return self.items.count

    def getSender(self):
        return self.sender

    def setSender(self, sender):
        self.sender = sender

    def getShipping(self):
        return self.shipping

    def setShipping(self, shipping):
        self.shipping = shipping
        
    def __unicode__(self):
        return "Transaction( " \
        "Code=%s, SenderEmail=%s, Date=%s, Reference=%s, status=%s, " \
        "itemsCount=%s)" % (self.code,self.email,self.date,self.reference,self.status)