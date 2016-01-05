//Problem Statement : https://www.hackerrank.com/challenges/funny-string
//ACCEPTED

#include<iostream>
#include<string>
#include<cmath>
using namespace std;

string rev(string s1);
int main(){
    int test;
    cin>>test;
for(int c=0;c<test;c++){
    string S;
    cin>>S;
    string R=rev(S);
    bool funny=true;
    for(int i=1;i<S.length();i++){
        int sn1=S[i];
        int sn2=S[i-1];
        int rn1=R[i];
        int rn2=R[i-1];
        if(abs(sn1-sn2)!=abs(rn1-rn2)){
            funny=false;
        }
    }
    if(funny){
        cout<<"Funny"<<endl;
    }else{
        cout<<"Not Funny"<<endl;
    }
}
}

string rev(string s1){
    string s2="";
    int j=s1.length()-1;
    for(int i=0;i<s1.length();i++){
        char ch=s1[j];
        s2.push_back(ch);
        j--;
    }
    return s2;
}
