class PagSeguroItem:
    _id = None
    description = None
    quantity = None
    amount = None
    weight = None
    shippingCost = None
    
    def __init__(self, data = None):
        if data:
            if 'id' in data:
                self.id = data['id']
            if 'description' in data:
                self.description = data['description']
            if 'quantity' in data:
                self.quantity = data['quantity']
            if 'amount' in data:
                self.amount = data['amount']
            if 'weight' in data:
                self.weight = data['weight']
            if 'shippingCost' in data:
                self.shippingCost = data['shippingCost']
                
    def getId(self):
        return self._id
    
    def setId(self, _id):
        self._id = _id
        
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description
        
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity):
        self.quantity = quantity
        
    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount
        
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight
        
    def getShippingCost(self):
        return self.shippingCost
    
    def setShippingCost(self, shippingCost):
        self.shippingCost = shippingCost