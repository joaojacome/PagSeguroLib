class PagSeguroTransactionSearchResult:

    date = None
    resultsInThisPage = None
    totalPages = None
    currentPage = None
    transactions = None

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getResultsInThisPage(self):
        return self.resultsInThisPage

    def setResultsInThisPage(self, resultsInThisPage):
        self.resultsInThisPage = resultsInThisPage

    def getTotalPages(self):
        return self.totalPages

    def setTotalPages(self, totalPages):
        self.totalPages = totalPages

    def getCurrentPage(self):
        return self.currentPage

    def setCurrentPage(self, currentPage):
        self.currentPage = currentPage

    def getTransactions(self):
        return self.transactions

    def setTransactions(self, transactions):
        self.transactions = transactions

    def __unicode__(self):
        return "PagSeguroTransactionSearchResult(Date=%s, " \
            "CurrentPage=%s, TotalPages=%s, " \
            "Transactions in this page=%s)" % (self.date, self.currentPage, self.totalpages, self.resultsInThisPage)