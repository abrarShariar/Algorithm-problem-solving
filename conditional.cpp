//SOLVED
#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    if(n%2==0){
        if(n>=2 && n<=5){
            cout<<"Not Weird"<<endl;
        }else if(n>=6 && n<=20){
            cout<<"Weird"<<endl;
        }else if(n>20){
            cout<<"Not Weird"<<endl;
        }
    }else{
        cout<<"Weird"<<endl;
    }

    return 0;
}
