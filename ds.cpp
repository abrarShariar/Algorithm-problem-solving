
#include<iostream>
using namespace std;

int main(){
    int arr[]={9,4,3,8,1,2};
    int len=sizeof(arr)/sizeof(arr[0]);

    for(int i=1;i<len;i++){
         int valInsert=arr[i];
         int valPos=i;
         while(valPos>0){
            if(arr[valPos-1]>arr[valPos]){
                arr[valPos]=arr[valPos-1];
            }
            valPos--;
         }
    }

    //output

    for(int i=0;i<len;i++){
        cout<<arr[i]<<endl;
    }
}


/*
int main(){
    int n;
    cin>>n;
    int arr[n];

    for(int i=0;i<n;i++){
        int num;
        cin>>num;
        arr[i]=num;
    }


    int len=sizeof(arr)/sizeof(arr[0]);
    bool isSorted=false;

    while(!isSorted){
        isSorted=true;
        for(int i=1;i<len;i++){
            if(arr[i-1]>arr[i]){
                isSorted=false;
                int temp=arr[i];
                arr[i]=arr[i-1];
                arr[i-1]=temp;
            }
        }
    }
    //output
    for(int i=0;i<len;i++){
        cout<<arr[i]<<endl;
    }
}
*/
