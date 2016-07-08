#include<iostream>
#include<map>
using namespace std;

int main(){

    map<int,int>myMap;
    myMap[1]=1;
    myMap[2]=0;
    myMap[3]=1;

    map<int,int>::iterator it;
    it=myMap.find(0);

    if(it!=myMap.end()){
        cout<<"FOUND";
    }else{
        cout<<"Not Found";
    }
}
