//4 test cases not passed
//TRY !!
//Code.cpp 4 - Pretty Print

#include<iostream>
#include<iomanip>
using namespace std;


int main(){
    int T;
    cin>>T;
    cout<<setiosflags(ios::uppercase | ios::showbase);
    cout<<setw(0xf)<<internal;

    while(T--){
    double A,B,C;
    cin>>A>>B>>C;
    //converting into Hexa
    cout<<setw(0);
    int iA=A;
    cout.flags(ios::left | ios::hex | ios::showbase);
    cout<<iA<<endl;

    //converting second condition
    cout.width(15);
    cout<<setprecision(2);
    cout<<fixed;
    cout<<setfill('_')<<right<<showpos<<B<<endl;
    cout<<noshowpos;

    //converting on third condition
    cout<<setw(0);
    cout.flags(ios::uppercase);
    cout<<setprecision(9);
    cout<<fixed;
    cout<<scientific;
    cout<<C<<endl;
    }
}
