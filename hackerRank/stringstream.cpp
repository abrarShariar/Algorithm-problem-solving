//Problem statement: https://www.hackerrank.com/challenges/c-tutorial-stringstream/submissions/code/15321095
//ACCEPTED


#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int>numbers;
    str=str+",";
    //vector<int>numbers;
    int f_index=0;
    int l_index;

    for(int i=0;i<str.length();i++){
        if(str[i]==','){
            int num;
            l_index=i;
            string s1=str.substr(f_index,l_index-f_index);

            stringstream(s1)>>num;
            numbers.push_back(num);
            f_index=l_index+1;
        }
    }
    return numbers;
}

int main() {
    string str;
    cin >> str;
    vector<int>integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}















/*
#include<iostream>
using namespace std;

int minArr(int *arr);
void cutStick(int *arr,int small);
void modifyStick(int *arr);
int total;

int main(){
    cin>>total;
    int arr[total];
    //input
    for(int i=0;i<total;i++){
        cin>>arr[i];
    }

    //processing
    bool exit=false;

    while(!exit){
        cout<<total<<endl;
        int small=minArr(arr);
        cutStick(arr,small);
        modifyStick(arr);
        if(total==0){
            exit=true;
        }
    }
}
void modifyStick(int *arr){
    int tempArr[total];
    int zero=0;
    for(int i=0;i<total;i++){
        tempArr[i]=arr[i];
        if(arr[i]==0){
            zero++;
        }
    }
    for(int i=0,j=0;i<total;i++){
        if(tempArr[i]!=0){
            arr[j]=tempArr[i];
            j++;
        }
    }
    total=total-zero;
}

void cutStick(int *arr,int small){
    for(int i=0;i<total;i++){
        arr[i]=arr[i]-small;
    }
}

int minArr(int *arr){
    int minNum=arr[0];
    for(int i=0;i<total;i++){
        if(arr[i]<minNum){
            minNum=arr[i];
        }
    }
    return minNum;
}

*/

