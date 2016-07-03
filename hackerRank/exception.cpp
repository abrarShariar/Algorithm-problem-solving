#include<iostream>
#include<exception>
#include<string>
#include<sstream>
using namespace std;

struct BadLengthException: public exception{
    char const *pchar;

public:
    BadLengthException(string temp_str){
        pchar=temp_str.c_str();
    };

    const char* what() const throw(){
        return pchar;
    }
};


int main(){
    stringstream ss;


    try{
        string name;
        cin>>name;
        if(name.length()<5){
            string temp;
            int len=name.length();
            ss<<len;
            ss>>temp;
            throw BadLengthException(temp);
        }
    }catch(BadLengthException e){
        cout<<e.what()<<endl;
    }

}
