//PROBLEM: https://www.hackerearth.com/problem/algorithm/array-manipulation-1-ba7785f4/description/
//ACCPETED
#include<iostream>
using namespace std;


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
//merge sort this shit
void mergeSort(int *arr, int l, int r){
    if(l<r){
        int mid = (l+r)/2;
        mergeSort(arr,l,mid);
        mergeSort(arr,mid+1,r);
        Merge(arr,l,mid,r);
    }
}


int main(){

    int T, capacity;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>capacity;
        int arr[capacity];
        cin.clear();
        for(int j=0;j<capacity;j++){
            cin>>arr[j];
        }

        //sort the array
        mergeSort(arr,0,capacity-1);
        int tempArr[capacity];

        //asc
        int z = 0;
        for(int i = 0;i<capacity;i+=2){
            tempArr[i] = arr[z];
            z++;
        }

        //desc
        int k = capacity - 1;
        for(int j=1;j<capacity;j+=2){
            if(k<z){
                break;
            }
            tempArr[j] = arr[k];
            k--;
        }

        //print
        for(int k=0;k<capacity;k++){
            cout<<tempArr[k]<<" ";
        }
        cout<<endl;
    }

}
