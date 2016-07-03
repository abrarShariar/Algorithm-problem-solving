
//Problem statement: https://www.hackerrank.com/challenges/staircase
//ACCEPTED


#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        for(int s=i;s<n-1;s++){
            cout<<" ";
        }
        for(int a=0;a<i+1;a++){
            cout<<"#";
        }
        cout<<endl;
    }
}
