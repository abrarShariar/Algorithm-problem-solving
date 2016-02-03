//SOLVED

#include<iostream>
//using namespace std;

int main(){

    //input
    int sz;
    std::cin>>sz;
    int arr[sz];
    for(int i=0;i<sz;i++){
        std::cin>>arr[i];
    }

    //proccess
    unsigned int res;
    for(int i=0;i<sz;i++){
        int reCount=0;
        int check=arr[i];
        for(int j=0;j<sz;j++){
            if(arr[j]==check){
                reCount++;
            }
        }
        if(reCount==1){
        res=check;
        break;
        }
    }
    std::cout<<res<<std::endl;
    return 0;
}
