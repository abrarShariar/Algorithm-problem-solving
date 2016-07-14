/*
    Project Euler - Problem #1
    SOLVED

    https://www.hackerrank.com/contests/projecteuler/challenges/euler001
*/

#include<iostream>

long int getLastElement(long int,long int);

int main(){

int test;
std::cin>>test;
for(int t=0;t<test;t++){
    long int N,count3,count5,count15,last3,last5,last15;
    std::cin>>N;

    //last element multiple of 3
    last3=getLastElement(N-1,3);
    last5=getLastElement(N-1,5);
    last15=getLastElement(N-1,15);

    count3=last3/3;
    count5=last5/5;
    count15=last15/15;

    long int sum3,sum5,sum15;
    sum3=(count3*(3+last3))/2;
    sum5=(count5*(5+last5))/2;
    sum15=(count15*(15+last15))/2;

    std::cout<<sum3+sum5-sum15<<std::endl;
}

}

long int getLastElement(long int N,long int index){
    bool isFound=false;
    while(!isFound){
        if(N%index==0){
            isFound=true;
            return N;
        }
        if(N<index){
            return 0;
        }
        N--;
    }
    return N;
}

