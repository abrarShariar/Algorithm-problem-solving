#include<iostream>
#include<string>
#include<map>
using namespace std;

class OperatorOverloadTest {
private:
    string number1;
    string number2;

public:
    OperatorOverloadTest();
    OperatorOverloadTest(OperatorOverloadTest &);
    OperatorOverloadTest(string, string);
    int operator + (OperatorOverloadTest &);
    string getNumber1();
    string getNumber2();

    map<string, int>strNumMap;
};

string OperatorOverloadTest::getNumber1() {
    return this->number1;
}

string OperatorOverloadTest::getNumber2() {
    return this->number2;
}

OperatorOverloadTest::OperatorOverloadTest(string number1, string number2) :
    number1(number1), number2(number2)
{
    cout << "Initializing object with: Number1: " << this->getNumber1() << " & " << " Number2: " << this->getNumber2() << endl;
    this->strNumMap["A"] = 10;
    this->strNumMap["B"] = 11;
    this->strNumMap["C"] = 12;
    this->strNumMap["D"] = 13;
    this->strNumMap["E"] = 14;
    this->strNumMap["F"] = 15;
}

// add the number1 together only
int OperatorOverloadTest::operator+(OperatorOverloadTest & rhs) {
    return this->strNumMap[this->getNumber1()] + rhs.strNumMap[rhs.getNumber1()];
}

int main () {
    OperatorOverloadTest oot("A", "B");
    OperatorOverloadTest oot2("C", "D");

    int result = oot + oot2;
    cout << "Result " << result << endl;

}