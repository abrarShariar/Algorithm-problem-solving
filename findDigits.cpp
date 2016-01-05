//Problem statement
//ACCEPTED

#include<iostream>
using namespace std;

int d_count(int num);
int div_count(int num);
int main(){
    int test,res;
    cin>>test;
    int res_arr[test];
for(int i=0;i<test;i++){
    int in;
    cin>>in;
    res=div_count(in);
    //cout<<res<<endl;
    res_arr[i]=res;
}

//output print
for(int j=0;j<test;j++){
    cout<<res_arr[j]<<endl;
    }
}

int div_count(int num){
    int chk=num;
    int ct=0;
    while(chk!=0){
        int rem=chk%10;
        chk=chk/10;
        if(rem==0){
            continue;
        }
        if(num%rem==0){
            ct++;
        }
    }
    return ct;
}

