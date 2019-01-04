// SOLVED: https://codeforces.com/contest/1095/problem/C
#include<bits/stdc++.h>
using namespace std;

int main () {
  int n,k;
  cin>>n>>k;

  map<int, int>ans;
  queue<int>q;

  for (int i=0;i<= 30;i++) {
    if (n & (1 << i)) {
      if (i > 0) {
        q.push(1 << i);
      }
      ans[1<<i]++;
    }
  }

  // // test print queue
  // for (int i=0;i<q.size();i++) {
  //   cout<<q.front()<<" ";
  //   q.pop();
  // }
  //
  // cout<<endl;

  // test print map
  // for (map<int, int>::iterator x = ans.begin();x != ans.end();x++) {
  //   cout<<x->first<<" "<<x->second<<endl;
  // }

  if (int(ans.size()) > k) {
    puts("NO");
    return 0;
  }

  int cnt = ans.size();

  while (cnt < k && !q.empty()) {
    int z = q.front();
    q.pop();
    ans[z] = ans[z] - 1;
    ans[z/2] += 2;
    if (z/2 > 1) {
      q.push(z/2);
      q.push(z/2);
    }
    cnt++;
  }

  if (cnt < k) {
    puts("NO");
    return 0;
  }

  puts("YES");
  for (map<int, int>::iterator x = ans.begin();x!= ans.end(); x++) {
    for (int i=0;i<x->second;i++) {
      cout<<x->first<<" ";
    }
  }
}
