#include<iostream>
using namespace std;

int re_sum(int,int);

int main(){
    int sum=re_sum(1,0);
    cout<<sum<<endl;
}

int re_sum(int num,int sum){

    if(num<=3){
        sum=num+re_sum(num+1,sum);
    }
    return sum;

}
