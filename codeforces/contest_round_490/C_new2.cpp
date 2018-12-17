// TIME LIMIT EXCEEDED - FIX IT
#include<iostream>
using namespace std;

int main() {
  int initial_alphabets[26];
  int out_alphabets[26];
  int n, k;

  for(size_t i = 0; i < 26; i++) {
    initial_alphabets[i] = 0;
  }

  cin>>n;
  cin>>k;

  char ch;
  int arr[n];
  for (size_t i = 0; i < n; i++) {
    cin>>ch;
    arr[i] = ch;
    int val = int(ch) - 97;
    initial_alphabets[val] = initial_alphabets[val] + 1;
  }

  for(size_t i = 0; i < 26; i++) {
    out_alphabets[i] = initial_alphabets[i];
  }

  int filter_index = 0;
  while (k > 0) {
    if(out_alphabets[filter_index] >= k) {
      out_alphabets[filter_index] = out_alphabets[filter_index] - k;
      k = 0;
    } else if (out_alphabets[filter_index] < k && out_alphabets[filter_index] > 0) {
      k = k - out_alphabets[filter_index];
      out_alphabets[filter_index] = 0;
      filter_index++;
    }
  }

  for(size_t i=0;i<n;i++){
    int digit = int(arr[i]) - 97;
    if(initial_alphabets[digit] == out_alphabets[digit]){
      cout<<char(arr[i]);
    } else {
      out_alphabets[digit] = out_alphabets[digit] + 1;
    }
  }
}
