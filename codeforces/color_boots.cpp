#include<iostream>
#include<map>
#include<vector>
using namespace std;

int main () {
  int t;
  cin>>t;
  map<char, vector<int> > firstBoot;
  map<char, vector<int> > secondBoot;
  vector<int>firstBootIndex;
  vector<int>secondBootIndex;
  char ch;
  // first boot
  for (int i=0;i<t;i++) {
    cin>>ch;
    firstBoot[ch].push_back(i);
  }

  // second boot
  for (int i=0;i<t;i++) {
    cin>>ch;
    secondBoot[ch].push_back(i);
  }
  // test
  // cout<<firstBoot['c'][0]<<endl;
  // cout<<firstBoot['c'][1]<<endl;

  // test
  // cout<<secondBoot['d'][0]<<endl;
  // cout<<secondBoot['d'][1]<<endl;
  int countPairs = 0;
  map<char, vector<int> >::iterator it;
  map<char, vector<int> >::iterator searchIt;
  for (it = firstBoot.begin(); it != firstBoot.end(); it++) {
    char testChar = it->first;
    if (testChar != '?') {
      searchIt = secondBoot.find(testChar);
      // cout<<it->first<<" "<<searchIt->first<<endl;
      if (searchIt != secondBoot.end()) {
        while (it->second.size() > 0) {
          if (searchIt->second.size() > 0) {
            int f1 = it->second.back();
            int f2 = searchIt->second.back();
            it->second.pop_back();
            searchIt->second.pop_back();
            firstBootIndex.push_back(f1);
            secondBootIndex.push_back(f2);
            countPairs++;
          } else {
            break;
          }
        }
      }
    }
  }

  // cout<<countPairs<<endl;
  // filter the question marks
  it = firstBoot.find('?');
  searchIt = secondBoot.find('?');
  // cout<<it->first<<endl;
  if (it != firstBoot.end()) {
    // ? marks found in firstBoot
    for (map<char, vector<int> >::iterator s = secondBoot.begin();s != secondBoot.end(); s++) {
      if (it->second.size() <= 0) {
        break;
      }
      if (s->first != '?') {
        while (s->second.size() > 0 && it->second.size() > 0) {
          int f1 = it->second.back();
          int f2 = s->second.back();
          firstBootIndex.push_back(f1);
          secondBootIndex.push_back(f2);
          it->second.pop_back();
          s->second.pop_back();
          countPairs++;
        }
      }
    }
  }

  if (searchIt != secondBoot.end()) {
    // ? marks found in secondBoot
    for (map<char, vector<int> >::iterator s = firstBoot.begin();s != firstBoot.end(); s++) {
      if (searchIt->second.size() <= 0) {
        break;
      }
      if (s->first != '?') {
        while (s->second.size() > 0 && searchIt->second.size() > 0) {
          int f1 = searchIt->second.back();
          int f2 = s->second.back();
          firstBootIndex.push_back(f2);
          secondBootIndex.push_back(f1);
          searchIt->second.pop_back();
          s->second.pop_back();
          countPairs++;
        }
      }
    }
  }

  // output print
  cout<<countPairs<<endl;
  for (int i=0;i<firstBootIndex.size();i++) {
    cout<<firstBootIndex[i] + 1<<" "<<secondBootIndex[i] + 1<<endl;
  }

}
