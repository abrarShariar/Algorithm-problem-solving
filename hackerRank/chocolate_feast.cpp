//Problem Statement: https://www.hackerrank.com/challenges/chocolate-feast
//ACCEPTED



#include<iostream>
using namespace std;

int choco_count(int cash,int per,int wrap);
int main(){

    int test;
    cin>>test;
    int cash,per,wrap,choc;
    int res[test];

   for(int i=0;i<test;i++){
        cin>>cash>>per>>wrap;
        int ch=choco_count(cash,per,wrap);
        res[i]=ch;
   }
   //print output
   for(int i=0;i<test;i++){
        cout<<res[i]<<endl;
   }
}

int choco_count(int cash,int per,int wrap){
    int choc=cash/per;
    int temp=choc;
    while(temp>=wrap){
        int more=temp/wrap;
        choc=choc+more;
        int rem=temp%wrap;
        temp=rem+more;
    }
    return choc;
}

