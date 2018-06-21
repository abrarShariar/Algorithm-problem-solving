//solved
#include<iostream>
using namespace std;

int main(){
    int n,k;
    cin>>n>>k;

    for(int i=0;i<k;i++){
        int lastDigit = n % 10;
        if(lastDigit > 0){
            n--;
        } else {
            n = n/10;
        }
    }

    cout<<n<<endl;
}
