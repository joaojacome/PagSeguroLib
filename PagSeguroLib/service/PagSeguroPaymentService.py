from PagSeguroLib.service.PagSeguroConnectionData import PagSeguroConnectionData
from PagSeguroLib.domain.PagSeguroHttpStatus import PagSeguroHttpStatus
from PagSeguroLib.exception.PagSeguroServiceException import PagSeguroServiceException
from PagSeguroLib.log.LogPagSeguro import LogPagSeguro
from PagSeguroLib.parser.PagSeguroPaymentParser import PagSeguroPaymentParser
from PagSeguroLib.utils.PagSeguroHttpConnection import PagSeguroHttpConnection
class PagSeguroPaymentService:
    serviceName = 'paymentService'
    
    @classmethod
    def buildCheckoutRequestUrl(cls, connectionData):
        return "%s/?%s" % (connectionData.getServiceUrl(), connectionData.getCredentialsUrlQuery())
    
    @classmethod
    def buildCheckoutUrl(cls, connectionData, code):
        return "%s?code=%s" % (connectionData.getResource('checkoutUrl'), code)
    
    @classmethod
    def createCheckoutRequest(cls, credentials, paymentRequest):
        LogPagSeguro.info("PagSeguroPaymentService.Register(%s) - begin" % paymentRequest)
        connectionData = PagSeguroConnectionData(credentials, cls.serviceName)
        
        try:
            connection = PagSeguroHttpConnection()
            connection.post(cls.buildCheckoutRequestUrl(connectionData), PagSeguroPaymentParser.getData(paymentRequest), connectionData.getServiceTimeout(), connectionData.getCharset())
            httpStatus = PagSeguroHttpStatus(connection.getStatus())
            httpStatusType = httpStatus.getType()
            if httpStatusType == 'OK':
                paymentParserData = PagSeguroPaymentParser.readSuccessXml(connection.getResponse())
                paymentUrl = cls.buildCheckoutUrl(connectionData, paymentParserData.getCode())
                LogPagSeguro.info("PagSeguroPaymentService.Register(%s) - end %s" % (paymentRequest, paymentParserData.getCode()))
            elif httpStatusType == 'BAD_REQUEST':
                errors = PagSeguroPaymentParser.readErrors(connection.getResponse())
                e = PagSeguroServiceException(httpStatus, errors)
                LogPagSeguro.info("PagSeguroPaymentService.Register(%s) - error %s" % (paymentRequest, e.getOneLineMessage()))
                raise e
            else:
                e = PagSeguroServiceException(httpStatus)
                LogPagSeguro.info("PagSeguroPaymentService.Register(%s) - error %s" % (paymentRequest, e.getOneLineMessage()))
                raise e
            if paymentUrl:
                return paymentUrl
            return False
        except:
            LogPagSeguro.error("Exception:")
            raise NameError("ERROR")
                
                
                
                
                