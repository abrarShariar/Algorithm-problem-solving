# demonstrate template string functions
from string import Template

def main():
	# Usual string formatting with format()
	str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
	print(str1)
	
	# TODO: create a template with placeholders
	temp1 = Template("You're watching ${title} by ${author}")
	# TODO: use the substitute method with keyword arguments
	str2 = temp1.substitute(title="Text", author="Abrar")
	print(str2)
	
	# TODO: use the substitute method with a dictionary

	
if __name__ == "__main__":
	main()
	