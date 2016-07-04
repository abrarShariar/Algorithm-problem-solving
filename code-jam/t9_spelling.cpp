/*
    T9 spelling

    SOLVED for small and large input
    https://code.google.com/codejam/contest/351101/dashboard#s=p2
*/

#include<iostream>
#include<map>
using namespace std;

map<char,string>keyPad;
string sequence;

char findKey(char);
int findStroke(char,char);

int main(){

    keyPad['2']="abc";
    keyPad['3']="def";
    keyPad['4']="ghi";
    keyPad['5']="jkl";
    keyPad['6']="mno";
    keyPad['7']="pqrs";
    keyPad['8']="tuv";
    keyPad['9']="wxyz";
    keyPad['0']=" ";

    //number of test cases
    int N;
    cin>>N;
    cin.ignore(256,'\n');
for(int t=0;t<N;t++){
    sequence="";
    //take user input
    string input;
    getline(cin,input);

    //proccess
    char key='$';
    for(int i=0;i<input.size();i++){
        char newKey=findKey(input[i]);
        int stroke=findStroke(newKey,input[i]);

        if(newKey==key){
            sequence.push_back(' ');
        }

        //prepare key sequence
        for(int j=0;j<stroke;j++){
            sequence.push_back(newKey);
        }
        key=newKey;
    }
    cout<<"Case #"<<t+1<<": "<<sequence<<endl;
    }
}

//find the number of strokes
int findStroke(char key,char in){
    int stroke=0;
    for(int i=0;i<keyPad[key].size();i++){
        if(keyPad[key].at(i)==in){
            stroke=i;
            break;
        }
    }
    return (stroke+1);
}


//find the key to press
char findKey(char in){
    if(in>='a' && in<='c'){
        return '2';
    }
    else if(in>='d' && in<='f'){
        return '3';
    }
    else if(in>='g' && in<='i'){
        return '4';
    }
    else if(in>='j' && in<='l'){
        return '5';
    }
    else if(in>='m' && in<='o'){
        return '6';
    }
    else if(in>='p' && in<='s'){
        return '7';
    }
    else if(in>='t' && in<='v'){
        return '8';
    }
    else if(in>='w' && in<='z'){
        return '9';
    }
    else if(in==' '){
        return '0';
    }
}
