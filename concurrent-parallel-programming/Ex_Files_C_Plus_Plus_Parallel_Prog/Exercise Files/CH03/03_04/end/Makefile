# Mutual Exclusion Demo Makefile
CXX		 = g++
CXXFLAGS = -Wall -std=c++11
TARGET	 = mutual_exclusion_demo
SRC		 = mutual_exclusion_demo.cpp

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET)