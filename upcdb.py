import requests

from requests import RequestException

class UPCDB():
	def __init__(self, apikey, api='https://api.upcdatabase.org/product'):
		self.apikey = apikey

		if api.endswith("/"):
			self.api = api
		else:
			self.api = '%s/' % (api)

	def get(self, upc):
		try:
			f = requests.get('%s%s?apikey=%s' % (self.api, upc ,self.apikey))
			return f.json()
		except RequestException as e:
			print(e)
			return {'success': 'false', 'reason': e.strerror}
