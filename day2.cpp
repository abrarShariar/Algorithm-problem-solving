//solved day 02 in 30 days of code

#include<iostream>
#include<limits>
#include<iomanip>
using namespace std;

int main(){
    int i=4;
    double d=4.0;
    string s="HackerRank ";

    int i2;
    double d2;
    string s2;

    cin>>i2>>d2;
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    getline(cin,s2);

    int res_i=i+i2;
    double res_d=d+d2;
    string res_s=s+s2;

    cout<<res_i<<endl;
    cout.precision(1);
    cout<<fixed<<res_d<<endl;
    cout<<res_s<<endl;

}
