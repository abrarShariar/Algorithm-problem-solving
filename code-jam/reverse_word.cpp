/*
    House Lannister

    SOLVED for small and large output
    https://code.google.com/codejam/contest/351101/dashboard#s=p1

*/

#include<iostream>
#include<ctype.h>
#include<vector>
using namespace std;

int main(){
    int test;
    cin>>test;
    int t;
    cin.ignore(256,'\n');
    for(t=0;t<test;t++){

        //int countW=0;
        bool endF=false;
        vector<string>strList;
        while(!endF){           //first loop takes a line input
            endF=false;
            string word;
            char in;

            while(true){        //second loop takes a word input
                in=cin.get();
                if(in=='\n'){
                    //cout<<"new"<<endl;
                    strList.push_back(word);
                    endF=true;
                    break;
                }
                else if(isspace(in)){
                    strList.push_back(word);
                    word="";
                }
                else{
                    word.push_back(in);     //insert char into word
                    //i++;
                }
            }
            if(endF){
                break;
            }
        }
        //test output
        //cout<<countW<<endl;
        cout<<"Case #"<<t+1<<": ";
        for(int i=strList.size()-1;i>=0;i--){
            cout<<strList[i]<<" ";
            //strList.pop_back();
        }
        cout<<endl;
    }
}
