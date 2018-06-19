#include<iostream>
#include<vector>
using namespace std;
//seg fault

void display(int *arr, int n) {
    for(int i=1;i<=n;i++){
        cout<<arr[i]<<" ";
    }
}


// Complete the arrayManipulation function below.
long arrayManipulation(int n, vector< vector<int> > queries) {
    //long long arr[n+1] = {0};

    vector< vector<int> >::iterator row;
    vector<int>::iterator col;
    long maxNum = 0;
    for(row = queries.begin(); row!= queries.end(); row++){
        col = row->begin();
        for(long j=*col;j<=*(col+1);j++){
            arr[j] += *(col+2);
            if(arr[j] > maxNum){
                maxNum = arr[j];
            }
        }
    }

    return maxNum;
}



int main(){

    int n,m;
    cin>>n>>m;
    vector< vector<int> > queries(m);


    for(int i=0;i<m;i++){
        queries[i].resize(3);
        for(int j=0;j<3;j++){
            cin>>queries[i][j];
        }
    }

    cout<<arrayManipulation(n,queries)<<endl;
    //print
    //display(arr,n);



}
