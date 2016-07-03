//selection sort

#include<iostream>
using namespace std;

int main(){

    int arr[]={14,33,27,10,35,19,42,44};
    int len=sizeof(arr)/sizeof(arr[0]);

    for(int i=0;i<len;i++){
        int small=arr[i];
        int pos=i;
        for(int j=i+1;j<len;j++){
            if(arr[j]<small){
                small=arr[j];
                pos=j;
            }
        }
        arr[pos]=arr[i];
        arr[i]=small;
    }

    //output
    for(int i=0;i<len;i++){
        cout<<arr[i]<<endl;
    }

}

