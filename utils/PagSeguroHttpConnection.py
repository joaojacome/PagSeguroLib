import urllib
import urllib2


class PagSeguroHttpConnection:
    
    status = None
    response = None
    
    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
        
    def getResponse(self):
        return self.response
    
    def setResponse(self, response):
        self.response = response
        
    def post(self, url, data, timeout=20, charset = 'ISO-8859-1'):
        return self.connect('POST', url, data, timeout, charset)
    
    def get(self, url, timeout=20, charset = 'ISO-8859-1'):
        return self.connect('GET', url, None, timeout, charset)
    
    def connect(self, method = 'GET', url = None, data = None, timeout = 20, charset = 'ISO-8859-1'):
        if url == None:
            raise NameError("url not set.")
            return False
        if method == "POST":
            if data:
                postFields = urllib.urlencode(data)
            else:
                postFields = ""
        else:
            postFields = ""
        
        #urrllib.getcode()
        try:
            headers = {
                "Content-length": "%s" % len(postFields),
                "Content-Type": "application/x-www-form-urlencoded; charset=%s" % charset,
            }
            if postFields == "":
                postFields = None
            req = urllib2.Request(url=url, data=postFields, headers=headers)
            retrieve = urllib2.urlopen(req)
            code = 200
        except urllib2.HTTPError, e:
            code = e.code
            raise NameError("Can't connect to %s. Error %d" % (url, e.code))
        
        self.setStatus(code)
        self.setResponse(retrieve.read())
        return True