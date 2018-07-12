//https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/magical-word/
//not accepted
#include<iostream>
#include <cmath>
using namespace std;

bool isPrime(int num) {
    bool prime = true;
    for(int i=2;i<=num/2;i++){
        if(num % i == 0){
            prime = false;
            break;
        }
    }
    return prime;
}

int main() {

    int tests, sz;
    char ch;
    cin>>tests;

    for(int i=0;i<tests;i++){
        cin>>sz;
        string s;
        cin>>s;
        for(int j=0;j<sz;j++){
            int key = (int) s[j];

            int rightKey = key;
            while(!isPrime(rightKey)){
                rightKey++;
            }

            int leftKey = key - 1;
            while(!isPrime(leftKey) && leftKey > 0){
                leftKey--;
            }

            if(abs(key - leftKey) > abs(key - rightKey)){
                ch = (char) rightKey;
            } else {
                ch = (char) leftKey;
            }
            cout<<ch;
        }
        cout<<endl;
    }


}
