# Atomic Variable Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = atomic_object_demo
SRC		 = atomic_object_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)