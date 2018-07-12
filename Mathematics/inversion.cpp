//solved:https://www.hackerrank.com/challenges/find-point/problem
#include<iostream>
#include<vector>
using namespace std;


vector<int> findPoint(int px, int py, int qx, int qy) {
    vector<int> result;
    int rx = 2*qx - px;
    int ry = 2*qy - py;
    result.push_back(rx);
    result.push_back(ry);
    return result;
}


int main(){

    vector<int> result = findPoint(1,1,2,2);

    for(int i=0;i<result.size();i++){
        cout<<result[i];

        if(i != result.size()){
            cout<<" ";
        }
    }
}
