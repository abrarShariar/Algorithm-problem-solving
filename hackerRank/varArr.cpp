//SOLVED
//https://www.hackerrank.com/challenges/variable-sized-arrays

#include<iostream>
using namespace std;

int main(){
    int N,Q;
    cin>>N>>Q;
    int* arr[N];

//take input for N lines
    for(int i=0;i<N;i++){
       int line;
       cin>>line;
       int *numArr=new int[line];
       arr[i]=numArr;

       for(int j=0;j<line;j++){
            int num;
            cin>>num;
            *(numArr+j)=num;
       }
    }

//Query
//loop for Q line
for(int i=0;i<Q;i++){
    int line;
    cin>>line;
    int *temp=arr[line];
    int index;
    cin>>index;

    cout<<*(temp+index)<<endl;

}

}
