//PROBLEM: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/aman-and-lab-file-work-8cd1d24c/description/
//accepted
#include<iostream>
using namespace std;

int CAPACITY = 0;

class Node {
    public:
        Node(){
            this->index = 0;
            this->totalTime = 0;
        }

        Node(int index, int totalTime) {
            this->index = index;
            this->totalTime = totalTime;
        };

    public:
        int index;
        int totalTime;
};


void display(Node arr[]) {
    /*
    for(int i=0;i<CAPACITY;i++){
        cout<<"Index: "<<arr[i].index<<" ";
        cout<<"Total Time: "<<arr[i].totalTime<<endl;
    }
    */
    for(int i=0;i<CAPACITY;i++){
        cout<<arr[i].index<<" ";
    }
}

//merge subroutine
void Merge(Node arr[], int l, int m, int r){
    int n1 = (m-l)+1;
    int n2 = r-m;

    Node lArr[n1];
    Node rArr[n2];

    for(int i=0;i<n1;i++){
        lArr[i] = arr[l+i];
    }

    for(int i=0;i<n2;i++){
        rArr[i] = arr[m+1+i];
    }

    int li=0,ri=0,ki=l;
    while(li<n1 && ri<n2){
        if(lArr[li].totalTime <= rArr[ri].totalTime){
            arr[ki] = lArr[li];
            li++;
        } else {
            arr[ki] = rArr[ri];
            ri++;
        }
        ki++;
    }

    while(li<n1){
        arr[ki] = lArr[li];
        li++;
        ki++;
    }

     while(ri<n2){
        arr[ki] = rArr[ri];
        ri++;
        ki++;
    }
}

//merge sort the shit out of it
void mergeSort(Node arr[], int l, int r) {
    if(l < r){
        int mid = (l+r)/2;
        mergeSort(arr,l,mid);
        mergeSort(arr,mid+1,r);
        Merge(arr,l,mid,r);
    }
}

int main(){

    cin>>CAPACITY;
    Node data[CAPACITY];
    int ti,di;

    for(int i=0;i<CAPACITY;i++) {
        cin>>ti;
        cin>>di;

        Node n1(i+1, ti+di);
        data[i] = n1;
    }

    //merge sort based on Node.totalTime
    mergeSort(data, 0, CAPACITY-1);

    display(data);
}
