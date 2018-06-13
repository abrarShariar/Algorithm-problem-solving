//PROBLEM: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-lucky-minimum-3/
//ACCEPTED

#include<iostream>
using namespace std;


//merge subroutine
void Merge(int *arr,int l, int m, int r){
    int i,j,k,temp[r-l+1];
    i=l;
    k=0;
    j=m+1;

    while(i <= m && j <= r){
        if(arr[i] < arr[j]){
            temp[k] = arr[i];
            k++;
            i++;
        } else {
            temp[k] = arr[j];
            k++;
            j++;
        }
    }

    while (i <= m){
		temp[k] = arr[i];
		k++;
		i++;
	}

	// Insert all the remaining values from j to high into temp[].
	while (j <= r){
		temp[k] = arr[j];
		k++;
		j++;
	}


	// Assign sorted data stored in temp[] to a[].
	for (i = l; i <= r; i++){
		arr[i] = temp[i-l];
	}
}

void mergeSort(int *arr, int l, int r){
    if(l < r){
        int mid = (l+r)/2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid+1, r);
        Merge(arr, l, mid, r);
    }
}

int main(){

    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        int capacity;
        cin>>capacity;
        int arr[capacity];
        for(int j=0;j<capacity;j++){
            cin>>arr[j];
        }
        //sort
        mergeSort(arr,0,capacity-1);
        //calculate freq
        int freq = 0;
        int m = 0;
        int minNum = arr[0];
        while(!(arr[m] > minNum) && m < capacity){
            freq++;
            m++;
        }

        if(freq%2 != 0 ){
            cout<<"Lucky"<<endl;
        } else {
            cout<<"Unlucky"<<endl;
        }
    }
}
