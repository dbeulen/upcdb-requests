import requests, json

from requests import RequestException

class UPCDB():
	class UPC():
		def __init__(self, data):
			if  'valid' in data and data.valid == "false":
				self.valid = False
			else:
				self.valid = True

			if 'reason' in data:
				self.reason      = data["reason"]
			else:
				self.name        = data["title"]
				self.number      = data["barcode"]
				self.description = data["description"]
				self.reason      = None

		def todict(self):
			return {'valid'       : self.valid,
					'reason'      : self.reason,
					'name'        : self.name,
					'number'      : self.number,
					'description' : self.description,
					}

	def __init__(self, apikey, api='https://api.upcdatabase.org/product'):
		self.apikey = apikey

		if api.endswith("/"):
			self.api = api
		else:
			self.api = '%s/' % (api)

	def get(self, upc):
		try:
			f = requests.get('%s%s?apikey=%s' % (self.api, upc ,self.apikey))
			print(f.json())
			return self.UPC(f.json())
		except RequestException as e:
			print(e)
			return self.UPC({'valid': 'false', 'reason': e.strerror})
