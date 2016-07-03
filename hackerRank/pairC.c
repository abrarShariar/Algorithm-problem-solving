//#include<iostream>
#include<stdio.h>

int main(){
    long long int test,testDiff;
    long long int counter=0;
    scanf("%lld %lld",&test,&testDiff);

    long long int numVec[test];
    auto i=0;
    for(i=0;i<test;i++){
         long long int num;
        scanf("%lld",&num);
        numVec[i]=num;
    }

    //calculate
    auto l=0,j=0;
    long long int pairDiff=0;
    for(l=0;l<test;l++){
        //long long int f1=numVec[i];
        for(j=l+1;j<test;j++){
                if(numVec[l]>=numVec[j]){
                    pairDiff=numVec[l]-numVec[j];
                }else{
                    pairDiff=numVec[j]-numVec[l];
                }

            if(pairDiff==testDiff){
                counter++;
            }
        }
    }
    printf("%lld",counter);
    return 0;
}

