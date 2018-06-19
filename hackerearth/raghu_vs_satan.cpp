//SOLVED:https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/practice-problems/algorithm/raghu-vs-sayan/

#include<iostream>
using namespace std;

void maxHeapify(int *arr, int start, int heapSize){
    int left = start*2;
    int right = start*2 + 1;
    int largest = start;
    if(left <= heapSize && arr[start] < arr[left]){
        largest = left;
    }
    if (right <= heapSize && arr[largest] < arr[right]) {
        largest = right;
    }

    if(arr[largest] != arr[start]){
        int temp = arr[largest];
        arr[largest] = arr[start];
        arr[start] = temp;
        maxHeapify(arr,largest,heapSize);
    }
}

void buildMaxHeap(int *arr, int heapSize){
    for(int i=heapSize/2;i>=1;i--){
        maxHeapify(arr,i,heapSize);
    }
}

void display(int *arr, int total){
    for(int i=1;i<=total;i++){
        cout<<arr[i]<<" ";
    }
}

void heapSort(int *arr, int N){
    int heapSize = N;
    for(int i=N;i>=2;i--){
        int temp = arr[1];
        arr[1] = arr[heapSize];
        arr[heapSize] = temp;
        heapSize--;
        maxHeapify(arr, 1, heapSize);
    }
}

int main(){

    int T;
    cin>>T;

    for(int i=0;i<T;i++){
              int rCap,sCap,totalDishes;
              cin>>rCap>>sCap>>totalDishes;
              int arr[totalDishes+1];
              arr[0] = -1;
              for(int k=1;k<totalDishes+1;k++){
                cin>>arr[k];
              }

              //heapsort arr
              buildMaxHeap(arr, totalDishes);
              heapSort(arr,totalDishes);
              //display(arr, totalDishes);

              int rFreq = 0,sFreq = 0;

              /*
              cout<<"sCap"<<sCap<<endl;
              cout<<"rCap"<<rCap<<endl;
              */

              for(int d=1;d<=totalDishes;d++){
                if(arr[d] <= rCap && rCap > 0){
                    rCap = rCap - arr[d];
                    rFreq++;
                }

                if(arr[d] <= sCap && sCap > 0){
                    sCap = sCap - arr[d];
                    sFreq++;
                }

                if(sCap <= 0 && rCap <= 0){
                    break;
                }
              }

              if(rFreq > sFreq){
                cout<<"Raghu Won"<<endl;
              } else if(sFreq > rFreq){
                cout<<"Sayan Won"<<endl;
              } else if (sFreq == rFreq){
                cout<<"Tie"<<endl;
              }
        }
}
