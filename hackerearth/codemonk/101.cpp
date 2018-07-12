//https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cipher-1/description/
//accepted
#include<iostream>
using namespace std;

char encrypt(int ch, int key, int low, int high){
    int newKey = ch + key;
    while(newKey > high){
        newKey = low + (newKey - high - 1);
    }
    return (char) newKey;
}

int main() {
    string s;
    cin>>s;
    int key, low, high;
    cin>>key;
    char ch;
    for(int i=0;i<s.length();i++) {
        if(s[i] >= 65 && s[i] <= 90){
            low = 65;
            high = 90;
        } else if (s[i] >= 97 && s[i] <= 122) {
            low = 97;
            high = 122;
        } else if (s[i] >= 48 && s[i] <= 57) {
            low = 48;
            high = 57;
        } else {
            cout<<s[i];
            continue;
        }

        ch = encrypt(s[i], key, low, high);
        cout<<ch;
    }
    return 0;
}
