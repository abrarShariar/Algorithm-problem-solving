#include<iostream>
using namespace std;

int main(){

    int T;
    cin>>T;

    for(int i=0;i<T;i++){
        int capacity;
        cin>>capacity;
        int arr[capacity];
        for(int k=0;k<capacity;k++){
            arr[k] = -1;
        }
        for(int j=0;j<capacity;j++){
            int input;
            cin>>input;
            if(input != -1){
                arr[input] = input;
            }
        }

        //print result
        for(int i=0;i<capacity;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
}
