import threading
import time

def thread_function (name):
	print("Thread {} starting".format(name))
	time.sleep(2)
	print("Thread {} ending".format(name))

if __name__ == "__main__":
	print("Before creating thread")
	x = threading.Thread(target=thread_function, args=("PyThread",))

	print("Before starting the thread")
	x.start()

	print("Ending thread")



