#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main(){
    ifstream read;
    read.open("input.txt");

     string text;
     string temp;
     getline(read,text);
     cout<<text<<endl;

     //cin>>text;
     int test;
     cin>>test;
     for(int i=0;i<test;i++){
            int f1,f2;
            cin>>f1>>f2;
            temp=text.substr(f1,f2+1);
            //reverse temp
            string rev="";
            for(int i=temp.length()-1;i>=0;i--){
                rev.push_back(temp[i]);
                    }
            //cout<<rev;
            //replace text
            text.replace(f1,f2+1,rev);
            cout<<text<<endl;
     }
     read.close();
}

    /*
    string text="Hello World";
    string reStr="C++";
    text.replace(0,5,reStr);
    cout<<text<<endl;
    */







