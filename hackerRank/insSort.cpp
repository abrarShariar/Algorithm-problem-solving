//insertion sort
#include<iostream>
using namespace std;

int main(){
    int arr[]={14,33,27,10,35,19,42,44};
    int len=sizeof(arr)/sizeof(arr[0]);

    for(int i=1;i<len;i++){
        int val=arr[i];
        int pos=i;
        for(int j=pos;j>0;j--){
            if(arr[j-1]>val){
                arr[j]=arr[j-1];
                arr[j-1]=val;
            }
        }
    }

    //output
    for(int i=0;i<len;i++){
        cout<<arr[i]<<endl;
    }
}
