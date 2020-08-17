#We have a local notion of a track because the json returned from spotify is freaking huge.
#Data necessary: uri and time
class Track:
	def __init__(self, uri, time):
		self.uri = uri
		self.time = time