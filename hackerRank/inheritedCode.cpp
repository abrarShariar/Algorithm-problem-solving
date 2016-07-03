//ACCEPTED in Code.cpp 04

#include <iostream>
#include <string>
#include <sstream>
#include <exception>
using namespace std;

//Exception define
struct BadLengthException: public exception{
    char const *pchar;

public:
    BadLengthException(int num){
        stringstream ss;
        string temp_str;
        ss<<num;
        ss>>temp_str;
        pchar=temp_str.c_str();
    };

    const char* what() const throw(){
        return pchar;
    }
};




bool checkUsername(string username){
    bool isValid=true;
    int n=username.length();
    if(n<5){
        throw BadLengthException(n);
    }
    for(int i=0;i<n-1;i++){
        if(username[i]=='w' && username[i+1]=='w'){
            isValid=false;
        }
    }
    return isValid;
}

int main(){
    int T;
    cin>>T;
    while(T--){
        string username;
        cin>>username;
        try{
            bool isValid=checkUsername(username);
            if(isValid){
                cout<<"Valid"<<'\n';
            }else{
                cout<<"InValid"<<'\n';
            }
        }catch(BadLengthException e){
            cout<<"Too short: "<<e.what()<<'\n';
        }
    }

    return 0;
}

