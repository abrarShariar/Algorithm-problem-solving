//#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>

int main(){
    std::vector<long double>numVec;

    long double test,testDiff;
     long int counter=0;
    scanf("%llf %llf",&test,&testDiff);

    for(auto i=0;i<test;i++){
         long double num;
        scanf("%llf",&num);
        numVec.push_back(num);
    }

    //calculate
    for(auto i=0;i<numVec.size();i++){
        //long long int f1=numVec[i];
        for(auto j=i+1;j<numVec.size();j++){
             long double pairDiff=std::abs(numVec[i]-numVec[j]);
            if(pairDiff==testDiff){
                counter++;
            }
        }
    }
    printf("%ld",counter);
}
