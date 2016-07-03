//Problem statement: https://www.hackerrank.com/challenges/angry-professor
//ACCEPTED



#include<iostream>
using namespace std;

int main(){
    int t_stu,p_stu,time;
    int line;
    cin>>line;
    string res[line];
//input
    for(int i=0;i<line;i++){
        int ct=0;
        cin>>t_stu>>p_stu;
        for(int i=0;i<t_stu;i++){
            cin>>time;
            if(time<=0){
            ct++;
            }
        }
        if(ct>=p_stu){
            res[i]="NO";
        }else{
            res[i]="YES";
        }
    }
//output
    for(int i=0;i<line;i++){
        cout<<res[i]<<endl;
    }
}
