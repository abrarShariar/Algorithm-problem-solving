//SOLVED
//30DaysOfCode

#include<iostream>
#include<fstream>
#include<map>
using namespace std;

int main(){
   map<string,int>phoneBook;
   string error="Not found";
   int n;
   cin>>n;
   cin.ignore(256,'\n');
   for(int i=0;i<n;i++){
    string name;
    cin>>name;
    int num;
    cin>>num;

    phoneBook[name]=num;
   }

    cin.ignore(256,'\n');
   //calculation
   while(true){
    string srch;
    getline(cin,srch);
    if(srch.empty()){
        break;
    }else{
        map<string,int>::iterator it;
        it=phoneBook.find(srch);
        if(it!=phoneBook.end()){
            cout<<it->first<<"="<<it->second<<endl;
        }else{
            cout<<error<<endl;
        }
    }
}
}
