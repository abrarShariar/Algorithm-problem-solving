#include<iostream>
using namespace std;

int main(){

    int test;
    cin>>test;
for(int i=0;i<test;i++){
        long int N,M,S;
    cin>>N>>M>>S;

    long int res=(N-S)+M;



    if(res>N){
        res=res-N;
    }else{
        res=(N-res)+M;
    }
    cout<<res+1<<endl;
}

}
