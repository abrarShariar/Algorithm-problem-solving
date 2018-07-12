#include<iostream>
using namespace std;

int main(){

    string s;
    for(int i=0;i<5;i++){
        string c;
        cin>>c;
        s.insert(i,c);
    }

    for(int i=0;i<s.length();i++){
        cout<<s[i]<<endl;
    }
}
