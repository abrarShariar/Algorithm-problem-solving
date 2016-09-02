/*
    SOLVED
    http://codeforces.com/problemset/problem/158/A
*/


#include<iostream>
//using namespace std;

int main(){
    int N,K;
    std::cin>>N>>K;
    int arr[N];
    for(int i=0;i<N;i++){
        std::cin>>arr[i];
    }

    //cout<<arr[K-1]<<endl;
    int countNext=0;
    for(int i=0;i<N;i++){
        if(arr[i]>=arr[K-1] && arr[i]!=0){
            countNext++;
        }
    }
    std::cout<<countNext<<std::endl;
}
