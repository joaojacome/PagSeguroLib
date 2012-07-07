from PagSeguroLib.utils.PagSeguroXmlParser import PagSeguroXmlParser
from PagSeguroLib.domain.PagSeguroError import PagSeguroError
class PagSeguroServiceParser:

    @classmethod
    def readErrors(cls, str_xml):
        parser = PagSeguroXmlParser(str_xml,'errors')
        data = parser.getResult('errors')
        errors = {}
        if 'error' in data and isinstance(data['error'], (list,tuple)):
            if 'code' in data['error'] and 'message' in data['error']:
                errors.append(PagSeguroError(data['error']['code'], data['error']['message']))
            else:
                for v in data['error']:
                    if 'code' in v and 'message' in v:
                        errors.append(PagSeguroError(v['code'], v['message']))
        return errors