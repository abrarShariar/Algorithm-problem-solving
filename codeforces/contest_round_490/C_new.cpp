//time limit exceded
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

    int n,k;
    cin>>n>>k;

    vector<char> charArr;
    vector<char>::iterator itVec;
    map<char, int> charMap;
    map<char, int>::iterator it;

    for(int i=0;i<n;i++) {
        char c;
        cin>>c;
        charArr.push_back(c);
        it = charMap.find(c);
        if(it == charMap.end()) {
            charMap.insert(pair<char,int>(c,1));
        } else {
            charMap[c] = it->second + 1;
        }
    }


    int delCounter = 0;
    it = charMap.begin();
    while(it != charMap.end() && delCounter < k){
        itVec = find(charArr.begin(), charArr.end(), it->first);
        if(itVec != charArr.end()) {
            //found
            charArr.erase(itVec);
            delCounter++;
        } else {
            it++;
        }
    }

    for(itVec = charArr.begin();itVec != charArr.end();++itVec){
        cout<<*itVec;
    }
}
