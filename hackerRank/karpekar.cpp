//ACCEPTED
//Problem Statement:https://www.hackerrank.com/challenges/kaprekar-numbers


#include<iostream>
#include<sstream>
#include<cmath>
using namespace std;

int getDigitCount(int);
int getRight(string,int);
int getLeft(string,int);
int getKaprekar(long long int);

int main(){

    //only for DEBUGGING
/*
    long long int num;
    cin>>num;
    cout<<getKaprekar(num)<<endl;
*/


    int upper,lower;
    cin>>lower>>upper;
    bool hasKaprekar=false;

    //loop over range
    for(int input=lower;input<=upper;input++){
        int kaprekar=getKaprekar(input);
        if(input==kaprekar){
            cout<<kaprekar<<" ";
            hasKaprekar=true;
        }
    }
    if(!hasKaprekar){
        cout<<"INVALID RANGE"<<endl;
    }




}


int getKaprekar(long long int num){
    int result=0;
    stringstream ss;
    string strNum;
    int numDigit=getDigitCount(num);
    long long int sqNum=num*num;
    ss<<sqNum;
    ss>>strNum;

    //cout<<strNum<<endl;

    int sqDigit=strNum.length();
    //cout<<sqDigit<<endl;
    int right=getRight(strNum,numDigit);
    //cout<<right<<endl;        //SUCCESS
    int left=getLeft(strNum,sqDigit-numDigit);
    //cout<<left<<endl;         //SUCCESS
    //cout<<right+left<<endl;
    result=right+left;
    return result;
}

//get right side of squared number
int getRight(string num,int digit){
    int result;
    string temp;
    string right="0";
    for(int rindex=num.length()-1;digit!=0;rindex--){
            //cout<<num[rindex];
            temp.push_back(num[rindex]);
            digit--;
    }

    for(int i=temp.length()-1;i>=0;i--){
        right.push_back(temp[i]);
    }
    //cout<<right<<endl;
    stringstream ss;
    ss<<right;
    ss>>result;
    return result;
}



//get left side number
int getLeft(string num,int digit){
        int result;
        string left="0";
        for(int i=0;i<digit;i++){
            left.push_back(num[i]);
        }
        stringstream ss;
        ss<<left;
        ss>>result;
        return result;
}

int getDigitCount(int num){
    int digit=0;
    while(num!=0){
        int rem=num%10;
        num=num/10;
        digit++;
    }
    return digit;
}
