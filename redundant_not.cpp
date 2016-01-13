//ACCEPTED


#include<iostream>
#include<vector>
//using namespace std;

int main(){
    int test;
    std::cin>>test;
    std::vector<int>data;
    for(int i=0;i<test;i++){
        bool isPresent=false;
        int num;
        std::cin>>num;
        for(int j=0;j<data.size();j++){
            if(num==data[j]){
                isPresent=true;
                break;
            }
        }
    if(!isPresent){
        std::cout<<"ADDED"<<std::endl;
        data.push_back(num);
    }else{
        std::cout<<"REDUNDANT"<<std::endl;
    }
    }


}
