//ACCEPTED
//problem statement: https://www.hackerrank.com/challenges/find-digits

#include<iostream>
using namespace std;

int main(){
    int test;
    cin>>test;
    for(int i=0;i<test;i++){
         int counter=0;
    int num;
    cin>>num;
    int temp=num;
    while(temp!=0){
        int rem=temp%10;
        temp=temp/10;
        if(rem==0){
            continue;
        }
        if(num%rem==0){
            counter++;
        }
    }
    cout<<counter<<endl;
    }
}
