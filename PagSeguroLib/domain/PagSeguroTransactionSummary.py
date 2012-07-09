class PagSeguroTransactionSummary:
    date = None
    lastEventDate = None
    code = None
    reference = None
    grossAmount = None
    _type = None
    status = None
    netAmount = None
    discountAmount = None
    feeAmount = None
    extraAmount = None
    paymentMethod = None
    


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

    def getGrossAmount(self):
        return self.grossAmount

    def setGrossAmount(self, grossAmount):
        self.grossAmount = grossAmount

    def getType(self):
        return self._type

    def setType(self, _type):
        self._type = _type

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getNetAmount(self):
        return self.netAmount

    def setNetAmount(self, netAmount):
        self.netAmount = netAmount

    def getDiscountAmount(self):
        return self.discountAmount

    def setDiscountAmount(self, discountAmount):
        self.discountAmount = discountAmount

    def getFeeAmount(self):
        return self.feeAmount

    def setFeeAmount(self, feeAmount):
        self.feeAmount = feeAmount

    def getExtraAmount(self):
        return self.extraAmount

    def setExtraAmount(self, extraAmount):
        self.extraAmount = extraAmount

    def getPaymentMethod(self):
        return self.paymentMethod

    def setPaymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod
