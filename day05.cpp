#include<iostream>
using namespace std;

int main(){
    char mul='x';
    int N;
    cin>>N;
    for(int i=1;i<=10;i++){
        int product=N*i;
        cout<<N<<' '<<mul<<' '<<i<<' '<<'='<<' '<<product<<endl;
    }

}
