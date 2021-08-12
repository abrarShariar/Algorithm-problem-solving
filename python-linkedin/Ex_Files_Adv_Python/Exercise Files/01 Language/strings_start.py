# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
	# define some starting values
	b = bytes([0x41, 0x42, 0x43, 0x44])
	print(b)
	print(type(b))

	s2 = b.decode('utf-8')
	print(s2)
	
	s = "This is a string"
	print(s)
	print(type(s))

	sb = s.encode('utf-32')
	print(sb)
	
	# TODO: Try combining them. 
	
	# TODO: Bytes and strings need to be properly encoded and decoded
	# before you can work on them together
	
	# TODO: encode the string as UTF-32
	
if __name__ == "__main__":
	main()
