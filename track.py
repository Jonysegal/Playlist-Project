#We have a local notion of a track because the json returned from spotify is freaking huge.
#Data necessary: uri and time
#we also track name for debugging purposes; afaik the name will serve no user purpose 
class Track:
	def __init__(self, uri, time, name):
		self.uri = uri
		self.time = time
		self.name = name