#include<iostream>
#include<sstream>
using namespace std;

int main(){
    stringstream ss;
    string strNum;
    int num;
    cin>>num;
    int sqNum=num*num;
    ss<<sqNum;
    ss>>strNum;
    int digit=strNum.length();


cout<<digit<<endl;

}
