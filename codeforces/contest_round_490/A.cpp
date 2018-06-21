//solved
#include<iostream>
using namespace std;

int main(){

    int n, k;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int leftIndex = 0;
    int rightIndex = n-1;

    int counter = 0;

    while(leftIndex < n){
        if(arr[leftIndex] <= k){
            leftIndex++;
        } else {
            break;
        }
    }

    counter = leftIndex;

    while(rightIndex >= 0 && counter < n){
        if(arr[rightIndex] <= k){
            rightIndex--;
            counter++;
        } else {
            break;
        }
    }

    cout<<counter<<endl;
}
