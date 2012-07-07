import os
from datetime import datetime
from PagSeguroLib.config.PagSeguroConfig import PagSeguroConfig 
from PagSeguroLib.singleton import Singleton
class LogPagSeguro(Singleton):
    
    log = None
    active = None
    fileLocation = None
    
    def __init__(self):
        self.reLoad()
    
    @classmethod
    def init(cls):
        if cls.log == None:
            cls.log = LogPagSeguro()
        return cls.log

    @classmethod
    def reLoad(cls):
        cls.active = PagSeguroConfig.logIsActive()
        if cls.active:
            fileLocation = PagSeguroConfig.getLogFileLocation()
            if os.path.exists(fileLocation) and os.path.isfile(fileLocation):
                cls.fileLocation = fileLocation
            else:
                cls.createFile()
    
    @classmethod
    def createFile(cls):
        if not cls.active:
            return False
        defaultPath = "" #PagSeguroLibrary.getPath()
        defaultName = 'PagSeguro.log'
        cls.fileLocation = os.path.join(defaultPath,defaultName)
        try:
            f = open(cls.fileLocation, 'a')
            f.close()
        except:
            raise "Can't create log file. Permission denied. File location: %s" % cls.fileLocation
        
    @classmethod
    def info(cls, message):
        cls.logMessage(message, 'info')
        
    @classmethod
    def warning(cls, message):
        cls.logMessage(message, 'warning')
    
    @classmethod
    def error(cls, message):
        cls.logMessage(message, 'error')
        
    @classmethod
    def debug(cls, message):
        cls.logMessage(message, 'debug')
        
    @classmethod
    def logMessage(cls, message, _type = None):
        if not cls.active:
            return False
        try:
            f = open(cls.fileLocation, "a")
        except:
            raise "Can't create log file. Permission denied. File location: %s" % cls.location
        
        date_message = "{%s}" % datetime.now().strftime("%d/%m/%y %H:%M:%S")
        type_message = ""
        if _type == 'info':
            type_message = "[Info]"
        elif _type == 'warning':
            type_message = "[Warning]"
        elif _type == 'error':
            type_message = "[Error]"
        else:
            message = "[Debug]"
        message = "%s %s %s\r\n" % (date_message, type_message, message)
        f.write(message)
        f.close()
    
    @classmethod
    def getHtml(cls, negativeOffset = None, reverse = None):
        if not cls.active:
            return False
        data = ""
        #TODO OFFSETS
        if os.path.exists(cls.fileLocation):
            f = open(cls.fileLocation,"r")
            data = f.read()
            data.replace("[","<strong>")
            data.replace("]","</strong>")
            data.replace("{","<span>")
            data.replace("}","</span>")
            data.replace("\r\n","<br/>\r\n")
        return data
    
