class Borg:
    
    """The Borg design pattern"""
	# attribute dictionary
	_shared_state = {}

	def __init__(self):
		self.__dict__ = self._shared_state
        

class Singleton(Borg): 
    
    """The singleton class"""
	
   

