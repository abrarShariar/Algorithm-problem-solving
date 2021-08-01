class Cache:
	_shared_cache = {}

class Singleton(Cache):

	def __init__(self, **kwargs):
		Cache.__init__(self)
		self._shared_cache.update(kwargs)

	def __str__(self):
		return str(self._shared_cache)


singleton = Singleton(name="Abrar")
print(singleton)

Singleton(skills=['C++', 'Python', 'Java'])

print(singleton)