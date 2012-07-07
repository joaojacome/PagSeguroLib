from PagSeguroLib.service.PagSeguroConnectionData import PagSeguroConnectionData
from PagSeguroLib.domain.PagSeguroHttpStatus import PagSeguroHttpStatus
from PagSeguroLib.helper.PagSeguroHelper import PagSeguroHelper
from PagSeguroLib.log.LogPagSeguro import LogPagSeguro
from PagSeguroLib.utils.PagSeguroHttpConnection import PagSeguroHttpConnection
from PagSeguroLib.parser.PagSeguroTransactionParser import PagSeguroTransactionParser
from PagSeguroLib.exception.PagSeguroServiceException import PagSeguroServiceException
class PagSeguroTransactionSearchService:
    serviceName = 'transactionSearchService'
    
    @classmethod
    def buildSearchUrlByCode(cls, connectionData, transactionCode):
        url = connectionData.getServiceUrl()
        return "%s/%s/?%s" % (url, transactionCode, connectionData.getCredentialsUrlQuery())
    
    @classmethod
    def buildSearchUrlByDate(cls, connectionData, searchParams):
        url = connectionData.getServiceUrl()
        if 'initialDate' in searchParams:
            initialDate = searchParams['initialDate']
        else:
            initialDate = None
        
        if 'finalDate' in searchParams:
            finalDate = "&finalDate=%s" % searchParams['finalDate']
        else:
            finalDate = None
            
        if 'pageNumber' in searchParams:
            page = "&page=%s" % searchParams['pageNumber']
        else:
            page = ""
        
        if 'maxPageResults' in searchParams:
            maxPageResults = "&maxPageResults=%s" % searchParams['maxPageResults']
        else:
            maxPageResults = ""
            
        return "%s/?%s&initialDate=%s%s%s%s" % (url, connectionData.getCredentialsUrlQuery(), initialDate, finalDate, page, maxPageResults)
    
    @classmethod
    def buildSearchUrlAbandoned(cls, connectionData, searchParams):
        url = connectionData.getServiceUrl()
        if 'initialDate' in searchParams:
            initialDate = searchParams['initialDate']
        else:
            initialDate = None
        
        if 'finalDate' in searchParams:
            finalDate = "&finalDate=%s" % searchParams['finalDate']
        else:
            finalDate = None
            
        if 'pageNumber' in searchParams:
            page = "&page=%s" % searchParams['pageNumber']
        else:
            page = ""
        
        if 'maxPageResults' in searchParams:
            maxPageResults = "&maxPageResults=%s" % searchParams['maxPageResults']
        else:
            maxPageResults = ""
            
        return "%s/abandoned/?%s&initialDate=%s%s%s%s" % (url, connectionData.getCredentialsUrlQuery(), initialDate, finalDate, page, maxPageResults)
    
    @classmethod
    def searchByCode(cls, credentials, transactionCode):
        LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByCode(%s) - begin" % transactionCode);
        connectionData = PagSeguroConnectionData(credentials, cls.serviceName)
        try:
            connection = PagSeguroHttpConnection()
            connection.get(cls.buildSearchUrlByCode(connectionData, transactionCode),connectionData.getServiceTimeout(), connectionData.getCharset())
            httpStatus = PagSeguroHttpStatus(connection.getStatus())
            httpStatusType = httpStatus.getType()
            if httpStatusType == 'OK':
                x = connection.getResponse()
                transaction = PagSeguroTransactionParser.readTransaction(x)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByCode(transactionCode=%s) - end %s" % (transactionCode, transaction))
            elif httpStatusType == 'BAD_REQUEST':
                errors = PagSeguroTransactionParser.readErrors(connection.getResponse())
                e = PagSeguroServiceException(httpStatus, errors)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByCode(transactionCode=%s) - error %s" % (transactionCode, e.getOneLineMessage()))
                raise e
            else:
                e = PagSeguroServiceException(httpStatus)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByCode(transactionCode=%s) - error %s" % (transactionCode, e.getOneLineMessage()))
                raise e
            if transaction:
                return transaction
            return False
        except:
            LogPagSeguro.error("Exception:")
            raise NameError("Error:")
        
    @classmethod
    def searchByDate(cls, credentials, pageNumber, maxPageResults, initialDate, finalDate = None):
        LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByDate(initialDate=%s, finalDate=%s) - begin" % (PagSeguroHelper.formatDate(initialDate), PagSeguroHelper.formatDate(finalDate)))
        connectionData = PagSeguroConnectionData(credentials, cls.serviceName)
        searchParams = {'initialDate': PagSeguroHelper.formatDate(initialDate),
                        'pageNumber': pageNumber,
                        'maxPageResults': maxPageResults }
        if finalDate:
            searchParams['finalDate'] = PagSeguroHelper.formatDate(searchParams['finalDate'])
        else:
            searchParams['finalDate'] = None
        
        try:
            connection = PagSeguroHttpConnection()
            connection.get(cls.buildSearchUrlByDate(connectionData, searchParams),connectionData.getServiceTimeout(), connectionData.getCharset())
            httpStatus = PagSeguroHttpStatus(connection.getStatus())
            httpStatusType = httpStatus.getType()
            if httpStatusType == 'OK':
                searchResult = PagSeguroTransactionParser.readSearchResult(connection.getResponse())
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByDate(initialDate=%s,finalDate=%s) - end %s" % (PagSeguroHelper.formatDate(initialDate),PagSeguroHelper.formatDate(finalDate), searchResult))
            elif httpStatusType == 'BAD_REQUEST':
                errors = PagSeguroTransactionParser.readErrors(connection.getResponse())
                e = PagSeguroServiceException(httpStatus, errors)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByDate(initialDate=%s,finalDate=%s) - error %s" % (PagSeguroHelper.formatDate(initialDate),PagSeguroHelper.formatDate(finalDate), e.getOneLineMessage()))
                raise e
            else:
                e = PagSeguroServiceException(httpStatus)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchByDate(initialDate=%s,finalDate=%s) - error %s" % (PagSeguroHelper.formatDate(initialDate),PagSeguroHelper.formatDate(finalDate), e.getOneLineMessage()))
                raise e
            if searchResult:
                return searchResult
            return False
        except e:
            LogPagSeguro.error("Exception: %s" % e.getMessage())
            raise e
        
    @classmethod
    def searchAbandoned(cls, credentials, pageNumber, maxPageResults, initialDate, finalDate = None):
        LogPagSeguro.info("PagSeguroTransactionSearchService.SearchAbandoned(initialDate=%s, finalDate=%s) - begin" % (PagSeguroHelper.formatDate(initialDate), PagSeguroHelper.formatDate(finalDate)))
        connectionData = PagSeguroConnectionData(credentials, cls.serviceName)
        searchParams = {'initialDate': PagSeguroHelper.formatDate(initialDate),
                        'pageNumber': pageNumber,
                        'maxPageResults': maxPageResults }
        if finalDate:
            searchParams['finalDate'] = PagSeguroHelper.formatDate(searchParams['finalDate'])
        else:
            searchParams['finalDate'] = None
        
        try:
            connection = PagSeguroHttpConnection()
            connection.get(cls.buildSearchUrlAbandoned(connectionData, searchParams),connectionData.getServiceTimeout(), connectionData.getCharset())
            httpStatus = PagSeguroHttpStatus(connection.getStatus())
            httpStatusType = httpStatus.getType()
            if httpStatusType == 'OK':
                searchResult = PagSeguroTransactionParser.readSearchResult(connection.getResponse())
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchAbandoned(initialDate=%s,finalDate=%s) - end %s" % (PagSeguroHelper.formatDate(initialDate),PagSeguroHelper.formatDate(finalDate), searchResult))
            elif httpStatusType == 'BAD_REQUEST':
                errors = PagSeguroTransactionParser.readErrors(connection.getResponse())
                e = PagSeguroServiceException(httpStatus, errors)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchAbandoned(initialDate=%s,finalDate=%s) - error %s" % (PagSeguroHelper.formatDate(initialDate),PagSeguroHelper.formatDate(finalDate), e.getOneLineMessage()))
                raise e
            else:
                e = PagSeguroServiceException(httpStatus)
                LogPagSeguro.info("PagSeguroTransactionSearchService.SearchAbandoned(initialDate=%s,finalDate=%s) - error %s" % (PagSeguroHelper.formatDate(initialDate),PagSeguroHelper.formatDate(finalDate), e.getOneLineMessage()))
                raise e
            if searchResult:
                return searchResult
            return False
        except e:
            LogPagSeguro.error("Exception: %s" % e.getMessage())
            raise e
            











