//Problem statement : https://www.hackerrank.com/challenges/sherlock-and-the-beast
//ACCEPTED


#include<iostream>
#include<sstream>
#include<math.h>
#include<cstdio>
using namespace std;

void makeNum(int n3,int n5);
int main(){
    int test;
    cin>>test;

for(int i=0;i<test;i++){

       int digit;
        cin>>digit;
        int n3=0;
        bool chk;
        for(int n5=digit;n5>=0;n5--){
            chk=true;
            if(n5%3==0 && n3%5==0){
                makeNum(n3,n5);
                cout<<endl;
                break;
            }else{
                chk=false;
            }
            n3++;
        }
        if(chk==false){
            cout<<-1<<endl;
        }
}
}

void makeNum(int n3,int n5){
    int total=n3+n5;
    char num[total];

   for(int i=0;i<n5;i++){
    num[i]='5';
   }
   for(int j=n5;j<total;j++){
    num[j]='3';
   }

   //print
   for(int i=0;i<total;i++){
    cout<<num[i];
   }
}



