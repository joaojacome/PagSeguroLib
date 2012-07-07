from PagSeguroLib.PagSeguro import PagSeguro
from PagSeguroLib.config.PagSeguroConfig import PagSeguroConfig
from PagSeguroLib.domain.PagSeguroAccountCredentials import PagSeguroAccountCredentials
from PagSeguroLib.service.PagSeguroTransactionSearchService import PagSeguroTransactionSearchService

transactionCode  = "00000000-0000-0000-0000-000000000000"
token = "00000000000000000000000000000000"
email = "email@email.com"
a = PagSeguro.init(email, token)
transaction = PagSeguroTransactionSearchService.searchByCode(a.config.getAccountCredentials(), transactionCode)
print transaction.getSender().getName()
