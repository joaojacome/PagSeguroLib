from PagSeguroLib.service.PagSeguroConnectionData import PagSeguroConnectionData
from PagSeguroLib.domain.PagSeguroHttpStatus import PagSeguroHttpStatus
from PagSeguroLib.exception.PagSeguroServiceException import PagSeguroServiceException
from PagSeguroLib.log.LogPagSeguro import LogPagSeguro
from PagSeguroLib.utils.PagSeguroHttpConnection import PagSeguroHttpConnection
from PagSeguroLib.parser.PagSeguroTransactionParser import PagSeguroTransactionParser

class PagSeguroNotificationService:
    
    serviceName = 'notificationService'
    
    @classmethod
    def buildTransactionNotificationUrl(cls, connectionData, notificationCode):
        url = connectionData.getServiceUrl()
        return "%s/%s/?%s" % (url, notificationCode, connectionData.getCredentialsUrlQuery())
    
    @classmethod
    def checkTransaction(cls, credentials, notificationCode):
        LogPagSeguro.info("PagSeguroNotificationService.CheckTransaction(notificationCode=%s) - begin" % notificationCode)
        connectionData = PagSeguroConnectionData(credentials, cls.serviceName)
        try:
            connection = PagSeguroHttpConnection()
            connection.get(cls.buildTransactionNotificationUrl(connectionData, notificationCode),connectionData.getServiceTimeout(),connectionData.getCharset())
            httpStatus = PagSeguroHttpStatus(connection.getStatus())
            httpStatusType = httpStatus.getType()
            if httpStatusType == 'OK':
                response = connection.getResponse()
                transaction = PagSeguroTransactionParser.readTransaction(response)
                #LogPagSeguro.info("PagSeguroNotificationService.CheckTransaction(notificationCode=%s) - end %s" % (notificationCode, transaction))
            elif httpStatusType == 'BAD_REQUEST':
                errors = PagSeguroTransactionParser.readErrors(connection.getResponse())
                e = PagSeguroServiceException(httpStatus, errors)
                LogPagSeguro.info("PagSeguroNotificationService.CheckTransaction(notificationCode=%s) - error %s" % (notificationCode, e.getOneLineMessage()))
                raise e
            else:
                e = PagSeguroServiceException(httpStatus)
                LogPagSeguro.info("PagSeguroNotificationService.CheckTransaction(notificationCode=%s) - error %s" % (notificationCode, e.getOneLineMessage()))
                raise e
            if transaction:
                return transaction
            return None
        except e:
            LogPagSeguro.error("Exception: %s" % e.getMessage())
            raise e
        
