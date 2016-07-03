//SOLVED
#include<iostream>
using namespace std;

int main(){

    int num;
    cin>>num;
    int countOne=0;
    int maxOne=0;

    while(num!=0){
        bool isOne=false;
        int rem=num%2;
        num=num/2;
        if(rem==1){
            isOne=true;
        }
        if(isOne){
            countOne++;
            if(countOne>maxOne){
                maxOne=countOne;
            }
        }else{
            countOne=0;
        }
    }
    cout<<maxOne<<endl;
}
