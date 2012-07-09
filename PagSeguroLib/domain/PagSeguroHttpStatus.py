class PagSeguroHttpStatus:
    typeList = {
        200: 'OK',
        400: 'BAD_REQUEST',
        401: 'UNAUTHORIZED',
        403: 'FORBIDDEN',
        404: 'NOT_FOUND',
        500: 'INTERNAL_SERVER_ERROR',
        502: 'BAD_GATEWAY'
    }
    status = None
    _type = None
    
    def __init__(self, status):
        self.status = status
        self._type = self.getTypeByStatus(status)
        
    def getType(self):
        return self._type
    
    def getStatus(self):
        return self.status
    
    def getTypeByStatus(self, status):
        if self.typeList[status]:
            return self.typeList[status]
        else:
            return False