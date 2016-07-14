#include<iostream>
using namespace std;

int main(){
    int test;
    cin>>test;
    for(int t=0;t<test;t++){

    long int N,M,S;
    cin>>N>>M>>S;
    long int poison=1;
    long int i=S;

    while(true){
        if(poison==M){
            break;
        }
        i=i+S;
        if(i>N){
            i=-1;
            continue;
        }

        poison++;
    }
    cout<<i<<endl;

    }

}
