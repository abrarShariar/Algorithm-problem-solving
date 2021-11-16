# Detached Thread Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = detached_thread_demo
SRC		 = detached_thread_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)