from PagSeguroLib.domain.PagSeguroCredentials import PagSeguroCredentials
class PagSeguroAccountCredentials(PagSeguroCredentials):
    email = None
    token = None
    
    def __init__(self, email, token):
        if email and token:
            
            self.email = email
            self.token = token
        else:
            raise NameError("Credentials not set.")
        
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
        
    def setToken(self, token):
        self.token = token
        
    def getAttributesMap(self):
        return {'email': self.email, 'token': self.token}
    
    def __unicode__(self):
        return "%s - %s" % (self.email, self.token)