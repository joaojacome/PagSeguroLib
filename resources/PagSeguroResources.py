from PagSeguroLib.singleton import Singleton
class PagSeguroResources(Singleton):
    resources = None
    data = {}
    varName = 'PagSeguroResources'
    
    @classmethod
    def __init__(cls):
        varName = cls.varName
        if varName:
            cls.data = varName
            del varName
        else: 
            raise NameError("Resources is undefined.")

    @classmethod
    def init(cls,data):
        if cls.resources == None:
            cls.resources = PagSeguroResources()
            cls.resources.data = data
        return cls.resources

    @classmethod
    def getData(cls, key1, key2 = None):
        if key2 != None:
            if key1 in cls.resources.data and key2 in cls.resources.data[key1]:
                return cls.resources.data[key1][key2]
            else:
                raise NameError("Resources keys %1, %2 not found." % (key1, key2))
        else:
            if key1 in cls.resources.data:
                return cls.resources.data[key1]
            else:
                raise NameError("Resources key %s not found." % key1)
    
    @classmethod
    def setData(cls, key1, key2, value):
        if key1 in cls.resources.data and key2 in cls.resources.data[key1]:
            cls.resources.data[key1][key2] = value
        else:
            raise NameError("Resources keys %1, %2 not found." % (key1, key2))
    
    @classmethod
    def getWebserviceUrl(cls, environment):
        if 'environment' in cls.resources.data and environment in cls.resources.data['environment'] and 'webserviceUrl' in cls.resources.data['environment'][environment]:
            return cls.resources.data['environment'][environment]['webserviceUrl']
        else:
            raise NameError("WebService URL not set for %s environment." % environment)