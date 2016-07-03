//Problem Statement :https://www.hackerrank.com/challenges/c-tutorial-pointer
//ACCEPTED

#include<iostream>
#include<cstdio>
using namespace std;

void update(int *a,int *b);
int main(){
   int n1,n2;
   cin>>n1>>n2;
   update(&n1,&n2);
   cout<<n1<<endl;
   cout<<n2<<endl;


}

void update(int *a,int *b){
    int temp=*a;
    *a=*a+*b;
    if(temp>*b){
        *b=temp-*b;
    }else{
        *b=*b-temp;
    }
}
