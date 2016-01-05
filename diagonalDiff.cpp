//Problem statement : https://www.hackerrank.com/challenges/diagonal-difference
//ACCEPTED




#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int n,num,s1=0,s2=0;
    //input
    cin>>n;
    int arr[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>num;
            arr[i][j]=num;
        }
    }
    for(int k=0,l=n-1;k<n;k++){
        s1=s1+arr[k][k];
        s2=s2+arr[k][l];
        l--;
    }
    int res=abs(s1-s2);
    cout<<res<<endl;
}




