//PROBLEM: https://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/

#include<iostream>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        string s;
        cin>>s;

        //reverse (no swap, no move)
        int si = 0;
        int ei = s.length() - 1;

        while(si < ei){
            int sEl = (int) s[si];
            int eEl = (int) s[ei];
            if((sEl >= 65 && sEl <= 90) || (sEl >= 97 && sEl <= 122)){
              if((eEl >= 65 && eEl <= 90) || (eEl >= 97 && eEl <= 122)){
                //swap
                int temp = s[si];
                s[si] = s[ei];
                s[ei] = temp;
                si++;
                ei--;
                continue;
              }
              ei--;
            } else {
                si++;
            }
        }

        cout<<s<<endl;
    }


}

