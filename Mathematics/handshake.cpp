//solved: https://www.hackerrank.com/challenges/handshake/problem
#include<iostream>
using namespace std;


int handshake(int n){

    int sum = 0;
    for(int i=1;i<=n;i++){
        sum += (n-i);
    }
    return sum;

}


int main(){

    int result = handshake(4);
    cout<<result<<endl;

}

