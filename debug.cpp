//reverse iterator
#include<iostream>
#include<sstream>

using namespace std;

int main(){
    //getting right digit

    string num="0";
    stringstream ss;
    ss<<num;
    int digi;
    ss>>digi;
    cout<<digi;




/*
    string temp;
    string right="";
    string left="";
    for(int rindex=num.length()-1;digit!=0;rindex--){
            //cout<<num[rindex];
            temp.push_back(num[rindex]);
            digit--;
    }

    for(int i=temp.length()-1;i>=0;i--){
        right.push_back(temp[i]);
    }
    //cout<<right<<endl;

    //getting left side number
    for(auto it=right.begin();it!=right.end();it++){
        num.erase(it);
    }
    cout<<num<<endl;
    */
}
