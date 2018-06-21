//SOLVED: https://codeforces.com/contest/977/problem/B

#include<iostream>
#include<map>
using namespace std;

int main(){

    int len;
    cin>>len;
    string s;
    cin>>s;

    map<string, int>oMap;
    for(int i=1;i<len;i++){
        string twoGram (s, i-1, 2);

        if(oMap.find(twoGram) != oMap.end()){
            //found -> increase
            int val = oMap[twoGram];
            oMap.at(twoGram) = val + 1;
        } else {
            oMap.insert(pair<string, int>(twoGram, 1));
        }
    }

    //sort based on key
    int maxValue = 0;
    string maxKey = "";
    for(map<string, int>::iterator it = oMap.begin();it!=oMap.end();++it){
        if(maxValue <= it->second){
            maxValue = it->second;
            maxKey = it->first;
        }
    }

    cout<<maxKey<<endl;

    //test print
    /*
    for(auto const& x : oMap){
        cout<<x.first<<" : "<<x.second<<endl;
    }
    */
}
