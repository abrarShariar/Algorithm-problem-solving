# Thread vs. Process Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = thread_process_demo
SRC		 = thread_process_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)