from PagSeguroLib.parser.PagSeguroServiceParser import PagSeguroServiceParser
from PagSeguroLib.utils.PagSeguroXmlParser import PagSeguroXmlParser
from PagSeguroLib.domain.PagSeguroTransactionSearchResult import PagSeguroTransactionSearchResult
from PagSeguroLib.domain.PagSeguroTransaction import PagSeguroTransaction
from PagSeguroLib.domain.PagSeguroPaymentMethod import PagSeguroPaymentMethod
from PagSeguroLib.domain.PagSeguroSender import PagSeguroSender
from PagSeguroLib.domain.PagSeguroShipping import PagSeguroShipping
from PagSeguroLib.domain.PagSeguroPhone import PagSeguroPhone
from PagSeguroLib.domain.PagSeguroAddress import PagSeguroAddress
from PagSeguroLib.domain.PagSeguroItem import PagSeguroItem
from PagSeguroLib.domain.PagSeguroTransactionSummary import PagSeguroTransactionSummary
class PagSeguroTransactionParser(PagSeguroServiceParser):
    
    @classmethod
    def readSearchResult(cls, xml):
        parser = PagSeguroXmlParser(xml, 'transactionSearchResult')
        data = parser.getResult('transactionSearchResult')
        
        searchResult = PagSeguroTransactionSearchResult()
        
        if 'totalPages' in data:
            searchResult.setTotalPages(data['totalPages'])
        
        if 'date' in data:
            searchResult.setDate(data['date'])
        
        if 'resultsinThisPage' in data:
            searchResult.setResultsInThisPage(data['resultsinThisPage'])
        
        if 'currentPage' in data:
            searchResult.setCurrentPage(data['currentPage'])
            
        if 'transactions' in data and isinstance(data['transactions'], (list, tuple)):
            transactions = {}
            for i, v in data['transactions']:
                if i == 'transaction':
                    transactions.append(cls.parseTransactionSummary(v))
            searchResult.setTransactions(transactions)
        return searchResult
    
    @classmethod
    def readTransaction(cls, xml):
        
        parser = PagSeguroXmlParser(xml)
        data = parser.getResult('transaction')
        
        transaction = PagSeguroTransaction()
        
        if 'lastEventDate' in data:
            transaction.setLastEventDate(data['lastEventDate'])
        
        if 'date' in data:
            transaction.setDate(data['date'])
        
        if 'code' in data:
            transaction.setCode(data['code'])
        
        if 'reference' in data:
            transaction.setReference(data['reference'])
            
        if 'type' in data:
            transaction.setType(data['type'])
            
        if 'status' in data:
            transaction.setStatus(data['status'])
            
        if 'paymentMethod' in data:
            paymentMethod = PagSeguroPaymentMethod()
            if 'type' in data['paymentMethod']:
                paymentMethod.setType(data['paymentMethod']['type'])
            if 'code' in data['paymentMethod']:
                paymentMethod.setCode(data['paymentMethod']['code'])
            transaction.setPaymentMethod(paymentMethod)
        
        if 'grossAmount' in data:
            transaction.setGrossAmount(data['grossAmount'])
            
        if 'discountAmount' in data:
            transaction.setDiscountAmount(data['discountAmount'])
            
        if 'feeAmount' in data:
            transaction.setFeeAmount(data['feeAmount'])
            
        if 'netAmount' in data:
            transaction.setNetAmount(data['netAmount'])
            
        if 'extraAmount' in data:
            transaction.setExtraAmount(data['extraAmount'])
            
        if 'installmentCount' in data:
            transaction.setInstallmentCount(data['installmentCount'])
            
        if data['items']['item'] and isinstance(data['items']['item'], (list,tuple)):
            items = {}
            i = 0
            for v in data['items']['item']:
                item = cls.parseTransactionItem(v)
                items[i] = item
                i = i + 1
                
            transaction.setItems(items)
        
        if 'sender' in data:
            sender = PagSeguroSender()
            if 'name' in data['sender']:
                sender.setName(data['sender']['name'])
            if 'email' in data['sender']:
                sender.setEmail(data['sender']['email'])
            if 'phone' in data['sender']:
                phone = PagSeguroPhone()
                if 'areaCode' in data['sender']['phone']:
                    phone.setAreaCode(data['sender']['phone']['areaCode'])
                if 'number' in data['sender']['phone']:
                    phone.setNumber(data['sender']['phone']['number'])
                sender.setPhone(phone)
            transaction.setSender(sender)
        
        if data['shipping'] and isinstance(data['shipping'], (list, tuple)):
            shipping = PagSeguroShipping()
            if 'type' in data['shipping']:
                shipping.setType(data['shipping']['type'])
            if 'cost' in data['shipping']:
                shipping.setCost(data['shipping']['cost'])
            if data['shipping']['address'] and isinstance(data['shipping']['address'],(list,tuple)):
                address = PagSeguroAddress()
                if 'street' in data['shipping']['address']:
                    address.setStreet(data['shipping']['address']['street'])
                if 'number' in data['shipping']['address']:
                    address.setNumber(data['shipping']['address']['number'])
                if 'complement' in data['shipping']['address']:
                    address.setComplement(data['shipping']['address']['complement'])
                if 'city' in data['shipping']['address']:
                    address.setCity(data['shipping']['address']['city'])
                if 'state' in data['shipping']['address']:
                    address.setState(data['shipping']['address']['state'])
                if 'district' in data['shipping']['address']:
                    address.setDistrict(data['shipping']['address']['district'])
                if 'postalCode' in data['shipping']['address']:
                    address.setPostalCode(data['shipping']['address']['postalCode'])
                if 'country' in data['shipping']['address']:
                    address.setCountry(data['shipping']['address']['country'])
                shipping.setAddress(address)
            transaction.setShipping(shipping)
        
        return transaction
            
            
    @classmethod
    def parseTransactionItem(self, data):
        item = PagSeguroItem()
        if 'id' in data:
            item.setId(data['id'])
        if 'description' in data:
            item.setDescription(data['description'])
        if 'quantity' in data:
            item.setQuantity(data['quantity'])
        if 'amount' in data:
            item.setAmount(data['amount'])
        if 'weight' in data:
            item.setWeight(data['weight'])
            
        return item
    
    @classmethod
    def parseTransactionSummary(cls, data):
        
        transactionSummary = PagSeguroTransactionSummary()
        if 'type' in data:
            transactionSummary.setType(data['type'])

        if 'code' in data:
            transactionSummary.setCode(data['code'])

        if 'reference' in data:
            transactionSummary.setReference(data['reference'])

        if 'date' in data:
            transactionSummary.setDate(data['date'])


        if 'lastEventDate' in data:
            transactionSummary.setLastEventDate(data['lastEventDate'])
        if 'grossAmount' in data:
            transactionSummary.setGrossAmount(data['grossAmount'])
        if 'status' in data:
            transactionSummary.setStatus(data['status'])
        if 'discountAmount' in data:
            transactionSummary.setDiscountAmount(data['discountAmount'])
            
        if 'feeAmount' in data:
            transactionSummary.setFeeAmount(data['feeAmount'])
            
        if 'netAmount' in data:
            transactionSummary.setNetAmount(data['netAmount'])
            
        if 'extraAmount' in data:
            transactionSummary.setExtraAmount(data['extraAmount'])

        if 'lastEvent' in data:
            transactionSummary.setLastEventDate(data['lastEvent'])

        if 'paymentMethod' in data and isinstance(data['paymentMethod'], (list, tuple)):
            paymentMethod = PagSeguroPaymentMethod()
            if 'paymentMethod' in data['type']:
                paymentMethod.setType(data['paymentMethod']['type'])
            if 'paymentMethod' in data['code']:
                paymentMethod.setCode(data['paymentMethod']['code'])
            transactionSummary.setPaymentMethod(paymentMethod)
            
        return transactionSummary
