from LRU import *

def test_LRU():
	cacheSize = 5
	lruCache = LRUCache(cacheSize)
	
	# insert first 5 items in the cache
	lruCache.insertData('A')
	print(f"Inserted block: {lruCache.getData('A')}")

	lruCache.insertData('B')
	print(f"Inserted block: {lruCache.getData('B')}")

	lruCache.insertData('C')
	print(f"Inserted block: {lruCache.getData('C')}")

	lruCache.insertData('D')
	print(f"Inserted block: {lruCache.getData('D')}")

	lruCache.insertData('E')
	print(f"Inserted block: {lruCache.getData('E')}")

	# check the most and least recently used (E, A)
	print(f"Most recently used: {lruCache.getMostRecentlyUsed()}")
	print(f"Least recently used: {lruCache.getLeastRecentlyUsed()}")


	# insert new block: X
	lruCache.insertData('X')
	print(f"Most recently used: {lruCache.getMostRecentlyUsed()}")

	# access an existing non-most-recently used block
	lruCache.insertData('D')
	print(f"Most recently used: {lruCache.getMostRecentlyUsed()}")
	# print Cache
	lruCache.printCache()

test_LRU()