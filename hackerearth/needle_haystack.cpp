//not accepted
//PROBLEM: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/a-needle-in-the-haystack-1/description/

#include<iostream>
using namespace std;

int hashMe(char c){
    return  c - 'a';
}

int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        int flag = 1;
        int f1[26] = {0};
        int f2[26] = {0};
        string s1,s2;
        cin>>s1;
        cin>>s2;

        for(int i=0;i<s1.length();i++){
            int index = hashMe(s1[i]);
            f1[index]++;
        }

        for(int i=0;i<s2.length();i++){
            int index = hashMe(s2[i]);
            f2[index]++;
        }

        for(int i=0;i<26;i++){
            if(f2[i] < f1[i]){
                flag = 0;
                break;
            }
        }

        if(flag == 1){
            cout<<"YES"<<endl;
        } else {
            cout<<"NO"<<endl;
        }
    }

}
