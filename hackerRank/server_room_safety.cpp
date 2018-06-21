#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;


int array_find_left(int *arr, int start, int limit, int val){
    for(int i=start;i<limit;i++){
        if(arr[i] == val){
            return i;
        }
    }
    return start+1;
}

int array_find_right(int *arr, int start, int limit, int val){
    for(int i=start;i>limit;i--){
        if(arr[i] == val){
            return i;
        }
    }

    return start-1;
}

int main(){
    int racks;
    cin>>racks;
    int pos[racks];
    int h[racks];
    sort(pos, pos+racks);
    for(int i=0;i<racks;i++) {
        cin>>pos[i];
    }

    for(int j=0;j<racks;j++) {
        cin>>h[j];
    }

    int checkLeft = 0;
    int checkRight = 0;

    //left
    int li = 0;
    while(li < racks - 1) {
        checkLeft = 0;
        int fallRange = pos[li] + h[li];
        if(fallRange >= pos[racks - 1]){
            checkLeft = 1;
            break;
        } else {
            if (fallRange < pos[li + 1] && li == 0) {
                checkLeft = 0;
                break;
            } else {
               li = array_find_left(pos, li, racks - 1, fallRange);
               checkLeft = 1;
               continue;
            }
        }
    }

   //cout<<"checkLeft: "<<checkLeft<<endl;

    //right
    int ri = racks - 1;
    while(ri > 0) {
        checkRight = 0;
        int fallRange = pos[ri] - h[ri];
        //cout<<"ri: "<<ri<<" fallRange: "<<fallRange<<" pos[ri] "<<pos[ri]<<" h[ri] "<<h[]<<endl;
        //cout<<fallRange<<endl;
        if(fallRange <= pos[0]){
            checkRight = 1;
            break;
        } else {
            if (fallRange > pos[ri - 1] && ri == racks - 1) {
                checkRight = 0;
                break;
            } else {
               ri = array_find_right(pos, ri, 0, fallRange);
               checkRight = 1;
               continue;
            }
        }
    }

    //cout<<"checkRight: "<<checkRight<<endl;
    //cout<<"checkLeft: "<<checkLeft<<endl;
    //cout<<"checkRight: "<<checkRight<<endl;


    if(checkLeft == 1 && checkRight == 1) {
        cout<<"BOTH"<<endl;
    } else if (checkLeft == 1 && checkRight != 1) {
        cout<<"LEFT"<<endl;
    } else if (checkRight == 1 && checkLeft != 1) {
        cout<<"RIGHT"<<endl;
    } else if (checkRight == 0 && checkLeft == 0){
        cout<<"NONE"<<endl;
    }
}
