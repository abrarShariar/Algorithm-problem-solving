# Shared Mutex Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = shared_mutex_demo
SRC		 = shared_mutex_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)