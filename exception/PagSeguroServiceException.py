from PagSeguroLib.domain.PagSeguroError import PagSeguroError
#from pagsegurolib.domain.PagSeguroHttpStatus import PagSeguroHttpStatus
class PagSeguroServiceException:
    httpStatus = None
    httpMessage = None
    errors = {}
    
    def __init__(self, httpStatus, errors = None):
        self.httpStatus = httpStatus
        if errors:
            self.errors = errors
        self.message = self.getFormatedMessage()
        
    def getErrors(self, errors): #???
        return self.errors
    
    def setErrors(self, errors):
        self.errors = errors
        
    def getHttpStatus(self):
        return self.httpStatus
    
    def setHttpStatus(self, httpStatus):
        self.httpStatus = httpStatus
        
    def getHttpMessage(self):
        a = self.httpStatus.getType()
        if a == 'BAD_REQUEST':
            message = 'BAD_REQUEST'
        elif a == 'UNAUTHORIZED':
            message = 'UNAUTHORIZED'
        elif a == 'FORBIDDEN':
            message = 'FORBIDDEN'
        elif a == 'NOT_FOUND':
            message = 'NOT_FOUND'
        elif a == 'INTERNAL_SERVER_ERROR':
            message = 'INTERNAL_SERVER_ERROR'
        elif a == 'BAD_GATEWAY':
            message = 'BAD_GATEWAY'
        else:
            message = 'UNDEFINED'
        return message
    
    def getFormatedMessage(self):
        message = "[HTTP %s] - %s\n" % (self.httpStatus.getStatus(), self.getHttpmessage)
        for v in self.errors:
            if isinstance(v, PagSeguroError):
                message = message + ("[%s] - %s" % (v.getCode(), v.getMessage()))
        return message
    
    def getOneLineMessage(self):
        return self.getFormatedMessage().replace("\n","")