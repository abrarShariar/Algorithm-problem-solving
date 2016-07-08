#include<iostream>
#include<math.h>
#include<cstdio>
#include<sstream>
#include<limits>
#include<iomanip>

using namespace std;

typedef std::numeric_limits<double>dbl;

//formula = (3+sqrt(5))^5
unsigned long getNumber(int);
int main(){

    int test;
    cin>>test;
for(int t=0;t<test;t++){

    int indice;
    cin>>indice;
    stringstream ss;
    unsigned long num=getNumber(indice);
    string str="";
    ss<<num;
    ss>>str;
    //cout<<str<<endl;
    char arr[3]={'0','0','0'};
    //cout<<str.size();
    int len=str.size();
    if(str.size()<3){
        for(int i=0;i<2;i++){
            arr[i]=str[len-1];
            len--;
        }
    }
    else{
        for(int i=0;i<3;i++){
            arr[i]=str[len-1];
            len--;
        }
    }

    //test output
    cout<<"Case #"<<t+1<<": ";
    for(int i=2;i>=0;i--){
        cout<<arr[i];
    }
    cout<<endl;
}
}

unsigned long getNumber(int index){
    long double ans;
    //double fv=setprecision(dbl::max_digits10) sqrt(5);
    long double num=3+sqrt(5);
    ans=pow(num,index);
    ans=(long) ans;
    return ans;
}
