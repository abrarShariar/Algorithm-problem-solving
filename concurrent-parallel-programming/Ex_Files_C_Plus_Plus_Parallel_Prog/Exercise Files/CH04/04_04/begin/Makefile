# Try Lock Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = try_lock_demo
SRC		 = try_lock_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)