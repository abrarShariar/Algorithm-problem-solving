/*
    Minimum Scalar Product
    SOLVED for small and big input

    https://code.google.com/codejam/contest/32016/dashboard#s=p0
*/

#include<iostream>
using namespace std;

void toAsc(long int* parr,int);
void toDesc(long int* parr,int);
long int getScalarProduct(long int*,long int*,int);

int main(){

    int testCase;
    cin>>testCase;
    //for each test case
    for(int t=0;t<testCase;t++){
        int numCount;
        cin>>numCount;
        long int vec1[numCount];
        long int vec2[numCount];
    //take input coordinates for vec 1
        for(int i=0;i<numCount;i++){
            cin>>vec1[i];
        }
    //take input coordinates for vec2
        for(int i=0;i<numCount;i++){
            cin>>vec2[i];
        }
    //ASC: vec1
        toAsc(vec1,numCount);
    //DESC: vec2
        toDesc(vec2,numCount);
        long int res=getScalarProduct(vec1,vec2,numCount);

        cout<<"Case #"<<t+1<<": "<<res<<endl;
   }

}

//return scalar product
long int getScalarProduct(long int *parr1,long int *parr2,int sz){
    long int sum=0;
    for(int i=0;i<sz;i++){
        sum+=parr1[i]*parr2[i];
    }
    return sum;
}

//sort in DESC
void toDesc(long int *parr,int sz){
    bool isSorted=false;
    while(!isSorted){
        isSorted=true;
        for(int i=1;i<sz;i++){
            if(parr[i-1]<parr[i]){
                isSorted=false;
                int temp=parr[i-1];
                parr[i-1]=parr[i];
                parr[i]=temp;
            }
        }
    }
}

//sort in ASC
void toAsc(long int* parr,int sz){
    bool isSorted=false;
    while(!isSorted){
        isSorted=true;
        for(int i=1;i<sz;i++){
            if(parr[i-1]>parr[i]){
                isSorted=false;
                int temp=parr[i-1];
                parr[i-1]=parr[i];
                parr[i]=temp;
            }
        }
    }
}
