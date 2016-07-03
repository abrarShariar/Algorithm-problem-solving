#include<iostream>
#include<fstream>
using namespace std;

int main(){
    ifstream read("A-small-practice.in");
    char c;


    //read.get(c)<<endl;

    while(read.get(c)){
        cout<<c;
    }

}





