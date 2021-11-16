# Data Race Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = data_race_demo
SRC		 = data_race_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)