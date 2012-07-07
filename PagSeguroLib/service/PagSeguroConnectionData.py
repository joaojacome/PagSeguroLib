from PagSeguroLib.config.PagSeguroConfig import PagSeguroConfig
from PagSeguroLib.resources.PagSeguroResources import PagSeguroResources
import urllib
class PagSeguroConnectionData:
    serviceName = None
    credentials = None
    resources = None
    environment = None
    webserviceUrl = None
    servicePath = None
    serviceTimeout = None
    charset = None
    
    def __init__(self, credentials, serviceName):
        self.credentials = credentials
        self.serviceName = serviceName
        self.setEnvironment(PagSeguroConfig.getEnvironment())
        self.setWebserviceUrl(PagSeguroResources.getWebserviceUrl(self.getEnvironment()))
        self.setCharset(PagSeguroConfig.getApplicationCharset())
        self.resources = PagSeguroResources.getData(self.serviceName)

        if 'servicePath' in self.resources:
            self.setServicePath(self.resources['servicePath'])
        
        if 'serviceTimeout' in self.resources:
            self.setServiceTimeout(self.resources['serviceTimeout'])
            
            
    def getCredentials(self):
        return self.credentials
    
    def setCredentials(self, credentials):
        self.credentials = credentials
        
    def getCredentialsUrlQuery(self):
        return urllib.urlencode(self.credentials.getAttributesMap())
    
    def getEnvironment(self):
        return self.environment
    
    def setEnvironment(self, environment):
        self.environment = environment
    
    def getWebserviceUrl(self):
        return self.webserviceUrl
    
    def setWebserviceUrl(self, webserviceUrl):
        self.webserviceUrl = webserviceUrl
        
    def getServicePath(self):
        return self.servicePath
    
    def setServicePath(self, servicePath):
        self.servicePath = servicePath
    
    def getServiceTimeout(self):
        return self.serviceTimeout
    
    def setServiceTimeout(self, serviceTimeout):
        self.serviceTimeout = serviceTimeout
        
    def getServiceUrl(self):
        return "%s%s" % (self.getWebserviceUrl(), self.getServicePath())
    
    def getResource(self, resource):
        return self.resources[resource]
    
    def getCharset(self):
        return self.charset
    
    def setCharset(self, charset):
        self.charset = charset