#include<iostream>
using namespace std;


void maxHeapify(int *Arr, int i, int N){
    int left = 2*i;
    int right = 2*i+1;
    int largest = i;

    if(left <= N && Arr[left] > Arr[i]){
        largest = left;
    }

    if(right <= N && Arr[right] > Arr[largest]){
        largest = right;
    }

    if(Arr[largest] != Arr[i]){
        //swap
        int temp = Arr[largest];
        Arr[largest] = Arr[i];
        Arr[i] = temp;
        //recursive heapify
        maxHeapify(Arr, largest, N);
    }
}

void buildMaxHeap(int *Arr, int N){
    for(int i=N/2;i>=1;i--){
        maxHeapify(Arr, i, N);
    }
}


void display(int *Arr, int N){
    for(int i=1;i<N+1;i++){
        cout<<Arr[i]<<" ";
    }
}

int main(){

    //input
    int N;
    cin>>N;
    int Arr[N+1];

    for(int i=1;i<N+1;i++){
        cin>>Arr[i];
    }

    //build heap
    buildMaxHeap(Arr,N);

    //print
    display(Arr, N);

}
