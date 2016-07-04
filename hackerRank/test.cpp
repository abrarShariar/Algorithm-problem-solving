#include<iostream>
#include<map>
using namespace std;

int main(){
    map<char,string>keyPad;
    keyPad['2']="abc";
    keyPad['3']="def";

    cout<<keyPad['2']<<endl;

}
