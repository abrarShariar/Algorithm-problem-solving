#include<iostream>
using namespace std;

int factorial(int);

int main(){
    int inN;
    cin>>inN;
    cout<<factorial(inN)<<endl;
}

int factorial(int N){
    if(N>0){
        return N*factorial(N-1);
    }else{
        return 1;
    }
}
