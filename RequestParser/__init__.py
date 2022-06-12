class init:
	def __init__(self, rawRequest:(str|dict) = None):
		self.rawRequest = rawRequest
		self.target = None
		self.method = None
		self.path = None
		self.params = None
		self.fragment = None
		self.headers = None
		self.cookies = None
		self.query = None
		self.data = None
		self.json = None
		self.files = None
		self.rawbody = None

		if type(rawRequest) == dict:
			if "target" in rawRequest: self.setTarget(rawRequest["target"])

			if "method" in rawRequest: self.setMethod(rawRequest["method"])

			if "path" in rawRequest: self.setPath(rawRequest["path"])

			if "params" in rawRequest: self.setParams(rawRequest["params"])

			if "fragment" in rawRequest: self.setFragment(rawRequest["fragment"])

			if "headers" in rawRequest and type(rawRequest["headers"]) == dict:
				for key,value in rawRequest["headers"].items():
					self.setHeaders(key, value)

			if "cookies" in rawRequest and type(rawRequest["cookies"]) == dict:
				for key,value in rawRequest["cookies"].items():
					self.setCookies(key, value)

			if "query" in rawRequest and type(rawRequest["query"]) == dict:
				for key,value in rawRequest["query"].items():
					self.setQuery(key, value)

			if "data" in rawRequest and type(rawRequest["data"]) == dict:
				pass

			if "json" in rawRequest and type(rawRequest["json"]) == dict:
				pass

			if "files" in rawRequest and type(rawRequest["files"]) == dict:
				pass

			if "rawbody" in rawRequest: self.setRawbody(rawRequest["rawbody"])

		elif type(self.rawRequest) == str and len(self.rawRequest) > 0:
			try:
				from urllib.parse import urlparse
			except Exception as e:
				from urlparse import urlparse

			tmp = self.rawRequest.split("\n")[0].split(" ")
			if len(tmp) == 3:
				if len(tmp[0]) != 0: self.setMethod(tmp[0])

				try:
					parse = urlparse(tmp[1])
					self.setPath(parse.path)
					self.setParams(parse.params)
					self.setFragment(parse.fragment)

					if len(parse.query) > 0:
						self.query = {}
						for q in parse.query.split("&"):
							self.setQuery(q.split("=", 1)[0], "") if len(q.split("=", 1)) == 1 else self.setQuery(q.split("=", 1)[0], q.split("=", 1)[1])
				except Exception as e:
					pass

			try:
				tmp = self.rawRequest.split("\n\n", 1)[0].split("\n")
				if len(tmp) > 1:
					self.headers = {}
					for header in tmp[1:]:
						self.setHeaders(header.split(": ", 1)[0], "") if len(header.split(": ", 1)) == 1 else self.setHeaders(header.split(": ", 1)[0], header.split(": ", 1)[1])

						if header.split(": ", 1)[0] == "Host":
							self.setTarget(header.split(": ", 1)[1])
			except Exception as e:
				pass



	def setTarget(self, target:str = None):
		self.target = str(target) if target != None and len(target) > 0 else None

	def setMethod(self, method:str = None):
		self.method = str(method) if method != None and len(method) > 0 else None

	def setPath(self, path:str = None):
		self.path = str(path) if path != None and len(path) > 0 else None

	def setParams(self, params:str = None):
		self.params = str(params) if params != None and len(params) > 0 else None

	def setFragment(self, fragment:str = None):
		self.fragment = str(fragment) if fragment != None and len(fragment) > 0 else None

	def setHeaders(self, key:str, value:str):
		if type(key) == str and type(value) == str:
			if self.headers == None:
				self.headers = {}

			if key == "Cookie":
				if len(value) > 0:
					self.clearCookies()
					for ck in value.split(";"):
						ck = ck.strip()
						if len(ck) > 0:
							self.setCookies(ck.split("=", 1)[0].strip(), "") if len(ck.split("=", 1)) == 1 else self.setCookies(ck.split("=", 1)[0].strip(), ck.split("=", 1)[1].strip())
			else:
				self.headers.update({key: value})

	def getHeaders(self, key:str) -> (None|str):
		if self.headers == None or key not in self.headers:
			return None
		return self.headers[key]

	def removeHeaders(self, key:str):
		if self.headers != None and key in self.headers:
			self.headers.pop(key)
			if len(self.headers) == 0:
				self.headers = None

	def clearHeaders(self):
		self.headers = None

	def setCookies(self, key:str, value:str):
		if type(key) == str and type(value) == str:
			if self.cookies == None:
				self.cookies = {}
			self.cookies.update({key: value})

	def getCookies(self, key:str) -> (None|str):
		if self.cookies == None or key not in self.cookies:
			return None
		return self.cookies[key]

	def removeCookies(self, key:str):
		if self.cookies != None and key in self.cookies:
			self.cookies.pop(key)
			if len(self.cookies) == 0:
				self.cookies = None

	def clearCookies(self):
		self.cookies = None

	def setQuery(self, key:str, value:str):
		if type(key) == str and type(value) == str:
			if self.query == None:
				self.query = {}
			self.query.update({key: value})

	def getQuery(self, key:str) -> (None|str):
		if self.query == None or key not in self.query:
			return None
		return self.query[key]

	def removeQuery(self, key:str):
		if self.query != None and key in self.query:
			self.query.pop(key)
			if len(self.query) == 0:
				self.query = None

	def clearQuery(self):
		self.query = None


	def setRawbody(self, rawbody:str = None):
		self.rawbody = str(rawbody) if rawbody != None and len(rawbody) > 0 else None

	def export(self) -> dict:
		return {
			"target": self.target,
			"method": self.method,
			"path": self.path,
			"params": self.params,
			"fragment": self.fragment,
			"query": self.query,
			"headers": self.headers,
			"cookies": self.cookies,
			"data": self.data,
			"json": self.json,
			"files": self.files,
			"rawbody": self.rawbody
		}