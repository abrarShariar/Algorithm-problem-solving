//Problem statement:https://www.hackerrank.com/challenges/plus-minus
//ACCEPTED


#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    int limit;
    double zero=0,pos=0,neg=0;
    //input
    cin>>limit;
    int arr[limit];
    for(int i=0;i<limit;i++){
        cin>>arr[i];
    }

    //calculate
    for(int i=0;i<limit;i++){
        if(arr[i]==0){
            zero++;
        }
        else if(arr[i]>0){
            pos++;
        }
        else{
            neg++;
        }
    }
    cout<<fixed<<setprecision(3);
    cout<<pos/limit<<endl;
    cout<<neg/limit<<endl;
    cout<<zero/limit<<endl;
}
