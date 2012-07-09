from PagSeguroLib.parser.PagSeguroServiceParser import PagSeguroServiceParser
from PagSeguroLib.utils.PagSeguroXmlParser import PagSeguroXmlParser
from PagSeguroLib.parser.PagSeguroPaymentParserData import PagSeguroPaymentParserData
from PagSeguroLib.helper.PagSeguroHelper import PagSeguroHelper
class PagSeguroPaymentParser(PagSeguroServiceParser):
    
    @classmethod
    def getData(cls, payment):
        data = {}
        if payment.getReference() != None:
            data['reference'] = payment.getReference()
        
        sender = payment.getSender()
        if sender != None:
            if sender.getName() != None:
                data['senderName'] = sender.getName()
            if sender.getEmail != None:
                data['senderEmail'] = sender.getEmail()
            
            if sender.getPhone() != None:
                if sender.getPhone().getAreaCode() != None:
                    data['senderAreaCode'] = sender.getPhone().getAreaCode()
                if sender.getPhone().getNumber() != None:
                    data['senderNumber'] = sender.getPhone().getAreaCode()
        if payment.getCurrency() != None:
            data['currency'] = payment.getCurrency()
        items = payment.getItems()
        if len(items) > 0:
            x=0
            for v in items:
                v = items[v]
                x = x + 1
                if v.getId() != None:
                    data["itemId%s" % x] = v.getId()
                    
                if v.getDescription() != None:
                    data["itemDescription%s" % x] = v.getDescription()
                
                if v.getQuantity() != None:
                    data["itemQuantity%s" % x] = v.getQuantity()

                if v.getAmount() != None:
                    data["itemAmount%s" % x] = PagSeguroHelper.decimalFormat(v.getAmount())
                    
                if v.getWeight() != None:
                    data["itemWeight%s" % x] = v.getWeight()
  
                if v.getShippingCost() != None:
                    data["itemShippingCost%s" % x] = PagSeguroHelper.decimalFormat(v.getShippingCost())
        if payment.getExtraAmount() != None:
            data['extraAmount'] = PagSeguroHelper.decimalFormat(payment.getExtraAmount())   

        if payment.getShipping() != None:
            if payment.getShipping.getType != None and payment.getShipping().getType().getValue() != None:
                data['shippingType']= payment.getShipping().getType().getValue()
            
            if payment.getShipping().getAddress != None:
                if payment.getShipping().getAddress().getStreet() != None:
                    data['shippingAddressStreet'] = payment.getShipping().getAddress().getStreet()
                    
                if payment.getShipping().getAddress().getNumber() != None:
                    data['shippingAddressNumber'] = payment.getShipping().getAddress().getNumber()
                    
                if payment.getShipping().getAddress().etComplement() != None:
                    data['shippingAddressComplement'] = payment.getShipping().getAddress().getComplement()
                    
                if payment.getShipping().getAddress().getCity() != None:
                    data['shippingAddressCity'] = payment.getShipping().getAddress().getCity()
                    
                if payment.getShipping().getAddress().getState() != None:
                    data['shippingAddressState'] = payment.getShipping().getAddress().getState()
                    
                if payment.getShipping().getAddress().getDistrict() != None:
                    data['shippingAddressDistrict'] = payment.getShipping().getAddress().getDistrict()
                    
                if payment.getShipping().getAddress().getPostalCode() != None:
                    data['shippingAddressPostalCode'] = payment.getShipping().getAddress().getPostalCode()
                    
                if payment.getShipping().getAddress().getCountry() != None:
                    data['shippingAddressCountry'] = payment.getShipping().getAddress().getCountry()
        
        if payment.getMaxAge() != None:
            data['maxAge'] = payment.getMaxAge()
            
        if payment.getMaxUses() != None:
            data['maxUses'] = payment.getMaxUses()
        if payment.getRedirectURL() != None:
            data['redirectURL'] = payment.getRedirectURL()
        return data
    
    @classmethod
    def readSuccessXml(cls, str_xml):
        parser = PagSeguroXmlParser(str_xml, 'checkout')
        data = parser.getResult('checkout')
        paymentParserData = PagSeguroPaymentParserData()
        paymentParserData.setCode(data['code'])
        paymentParserData.setRegistrationDate(data['date'])
        return paymentParserData
