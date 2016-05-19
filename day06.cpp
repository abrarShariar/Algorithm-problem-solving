//SOlVED on 30daysOfCode
//Day 06
#include<iostream>
using namespace std;

int main(){

    int n;
    cin>>n;
    cin.ignore(256,'\n');

    for(int i=0;i<n;i++){
        string even="";
        string odd="";
        string str;
        getline(cin,str);
        for(int j=0;j<str.length();j++){
            if(j%2==0){
                even+=str[j];
            }else{
                odd+=str[j];
            }
        }
        cout<<even<<' '<<odd<<endl;
    }
}
