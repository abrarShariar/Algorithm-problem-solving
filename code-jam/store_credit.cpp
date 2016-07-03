#include<iostream>
#include<fstream>
using namespace std;

int Credit,List,n2,testCase;
int index1=0,index2=0;

int main(){
    cin>>testCase;
    for(int t=0;t<testCase;t++){
        index1=0;
        index2=0;
        cin>>Credit>>List;
        int Price[List];

    //take input of prices
        for(int i=0;i<List;i++){
            cin>>Price[i];
        }
    //proccess
    bool isFound;
    int check;
    for(int i=0;i<List;i++){
        isFound=false;
        check=Price[i];
        index1=i;
        if(check<Credit){
            for(int j=i+1;j<List;j++){
            if(Price[j]==(Credit-check)){
                index2=j;
                isFound=true;
                break;
                }
            }
        }
        if(isFound){
            break;
        }
    }

    cout<<"Case #"<<t+1<<": ";
    //output
    if(index1>index2){
        cout<<index2+1<<" "<<index1+1<<endl;
    }else{
        cout<<index1+1<<" "<<index2+1<<endl;
    }
}

}



