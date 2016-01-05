//Problem :  https://www.hackerrank.com/challenges/time-conversion
//ACCEPTED

#include<iostream>
#include<sstream>
#include<string>
using namespace std;

int main(){
    bool convert=false;
    string s1;
    stringstream ss;
    //input
    getline(cin,s1);
    for(int i=0;i<s1.length();i++){
        if(s1[i]=='P'){
            convert=true;
            break;
        }
    }
    //convert
        int num;
        string s2=s1.substr(0,2);
        ss<<s2;
        ss>>num;
        stringstream ss2;

    if(convert){
        if(num!=12){
            num=num+12;
            ss2<<num;
            ss2>>s2;
            s1=s2+s1.substr(2,6);
        }else{
            s1=s1.substr(0,8);
        }
    }else{
        if(num==12){
            s2="00";
            s1=s2+s1.substr(2,6);
        }else{
        s1=s1.substr(0,8);
        }
    }

    cout<<s1<<endl;
}
