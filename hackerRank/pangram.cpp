//Problem statement : https://www.hackerrank.com/challenges/pangrams
//ACCEPTED

#include<iostream>
#include<cctype>
using namespace std;

bool check_pangram(string text);
int main(){
    string text;
    getline(cin,text);
    if(check_pangram(text)){
        cout<<"pangram"<<endl;
    }else{
        cout<<"not pangram"<<endl;
    }
}

bool check_pangram(string text){
    bool pangram=true;
    int arr[30];
    int j=0;
    for(int i=97;i<=122;i++){
        arr[j]=i;
        j++;
    }

    //loop for text
    for(int k=0;k<text.length();k++){
        int asc=tolower(text[k]);
        //loop  through arr
        for(int a=0;a<26;a++){
            if(arr[a]==asc){
                arr[a]=0;
                break;
            }
        }
    }
    for(int i=0;i<26;i++){
        if(arr[i]!=0){
            pangram=false;
            break;
        }
    }
    return pangram;
}

