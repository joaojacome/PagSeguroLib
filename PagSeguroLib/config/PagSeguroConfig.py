from PagSeguroLib.singleton import Singleton
from PagSeguroLib.domain.PagSeguroAccountCredentials import PagSeguroAccountCredentials

class PagSeguroConfig(Singleton):
    config = None
    data = {}
    
    
    @classmethod
    def init(cls, data):
        if cls.config == None:
            cls.config = PagSeguroConfig()
            cls.data = data
        return cls.config
    
    @classmethod
    def getData(cls, key1, key2 = None):
        if key2 != None:
            if key1 in cls.data and key2 in cls.data[key1]:
                return cls.data[key1][key2]
            else:
                raise NameError("Config keys %s, %s not found." % (key1, key2))
        else:
            if key1 in cls.data:
                return cls.data[key1]
            else:
                raise NameError("Config key %s not found." % key1)

    @classmethod
    def getAccountCredentials(cls):
        if 'credentials' in cls.data and 'email' in cls.data['credentials'] and 'token' in cls.data['credentials']:
            return PagSeguroAccountCredentials(cls.data['credentials']['email'],cls.data['credentials']['token'])
        else:
            raise NameError("Credentials not set.")
        
    @classmethod
    def setData(cls, key1, key2, value):
        if key1 in cls.data and key2 in cls.data[key1]:
            cls.data[key1][key2] = value
        else:
            raise NameError("Config keys %s, %s not found." % (key1, key2))
    
    @classmethod
    def getEnvironment(cls):
        if cls.data['environment'] and cls.data['environment']['environment']:
            return cls.data['environment']['environment']
        else:
            raise NameError("Environment not set")
    
    @classmethod
    def getApplicationCharset(cls):
        if cls.data['application'] and cls.data['application']['charset']:
            return cls.data['application']['charset']
        else:
            raise NameError("Application charset not set")
    
    @classmethod
    def setApplicationCharset(cls, charset):
        cls.setData('application','charset',charset)

    @classmethod
    def logIsActive(cls):
        if 'log' in cls.data and 'active' in cls.data['log'] and cls.data['log']['active'] == True:
            return True
        return False
        #raise NameError("Log activation flag not set.")
        
    @classmethod
    def activeLog(cls, fileName=None):
        cls.setData('log','active',True)
        if fileName:
            cls.setData('log','fileLocation',fileName)
        else:
            cls.setData('log','fileLocation','')
        #TODO
        #LOG RELOAD
        
    @classmethod
    def getLogFileLocation(cls):
        if 'log' in cls.data and 'fileLocation' in cls.data['log']:
            return cls.data['log']['fileLocation']
        else:
            raise NameError("Log file location not set.")
        
