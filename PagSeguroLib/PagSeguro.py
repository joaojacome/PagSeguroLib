from PagSeguroLib.singleton import Singleton
from PagSeguroLib.config.PagSeguroConfig import PagSeguroConfig
from PagSeguroLib.log.LogPagSeguro import LogPagSeguro
from PagSeguroLib.resources.PagSeguroResources import PagSeguroResources
class PagSeguro(Singleton):
	library = None
	resources = None
	config = None
	log = None
	
	@classmethod
	def init(cls, email, token):
		if cls.library == None:
			cls.library = PagSeguro(email, token)
		return cls.library
	
	def __init__(self, email, token):
		resources = {
			'environment': {
				'production': {
					'webserviceUrl': "https://ws.pagseguro.uol.com.br"
				}		
			},
			'paymentService' : {
				'servicePath': "/v2/checkout",
				'checkoutUrl': "https://pagseguro.uol.com.br/v2/checkout/payment.html",
				'serviceTimeout': 20
			},
			'notificationService': {
				'servicePath': "/v2/transactions/notifications",
				'serviceTimeout': 20
			},
			'transactionSearchService': {
				'servicePath': "/v2/transactions",
				'serviceTimeout': 20
			}
		}
		configs = {
			'environment': {
				'environment': "production"
			},
			'credentials': {
				'email': email,
				'token': token
			},
			'application': {
				'charset': "ISO-8859-1"
			},
			'log': {
				'active': False,
				'fileLocation': ""
			}
		}
		self.resources = PagSeguroResources.init(resources)
		self.config = PagSeguroConfig.init(configs)
		self.log = LogPagSeguro.init()
