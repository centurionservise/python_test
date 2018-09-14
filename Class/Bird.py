class Bird :

	'''A base class to define bird properties.'''

	count = 0

	def __init__( self , chat ) :

		self.sound = chat
		Bird.count += 1
		self.self_count=Bird.count

	def talk( self ) :

		return self.sound
	
	def counter(self):
		return self.self_count


