
class PagSeguroError:
    code = None
    message = None
    
    def __init__(self, code, message):
        self.code = code
        self.message = message
    
    def getCode(self):
        return self.code
    
    def setCode(self, code):
        self.code = code
        
    def getMessage(self):
        return self.message
    
    def setMessage(self, message):
        self.message = message
        
        