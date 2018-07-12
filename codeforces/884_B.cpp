//http://codeforces.com/problemset/problem/884/B
//accepted
#include<iostream>
using namespace std;

int main(){
    int seg,len;
    cin>>seg>>len;

    int arr[seg];
    int totalSpace = 0;
    for(int i=0;i<seg;i++){
        int s;
        cin>>s;
        if(i != seg - 1){
            totalSpace += s + 1;
        } else {
            totalSpace += s;
        }
    }

    if(totalSpace > len){
        cout<<"NO"<<endl;
        return 0;
    } else if(totalSpace == len) {
        cout<<"YES"<<endl;
    } else if(totalSpace < len) {
        cout<<"NO"<<endl;
    }
}
