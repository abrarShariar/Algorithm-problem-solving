// https://www.hackerrank.com/challenges/attribute-parser/problem

#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
  map<string, string> tag_mapping;

  // input
  int N, Q;
  cin>>N>>Q;
  cin.ignore();

  // filter
  for (int i=0;i<N;i++) {
    string line;
    getline(cin, line);
    if (line[1] != '/') {
      line.erase(0,1);
      line.erase(line.length() - 1);
      // check for the first space. if no space then no attribute
      size_t space_found = line.find_first_of(" ");
      if (space_found != string::npos) {
        string tag = line.substr(0, space_found);
        string body = line.substr(space_found+1);
        tag_mapping[tag] = body;
      }
    }
  }

  // cout<<tag_mapping["tag1"]<<endl;
  // input queries

  for (int i = 0;i<Q;i++) {
    string line;
    getline(cin, line);
    size_t tilde_found = line.find_first_of('~');
    string attribute = line.substr(tilde_found+1);
    string tag;
    // filter tag
    int index = tilde_found - 1;
    while (index >=0) {
      if (line[index] == '.') {
        break;
      }
      index--;
    }

    if (index > 0) {
      tag = line.substr(index+1, tilde_found - (index+1));
    } else {
      tag = line.substr(0, tilde_found);
    }

    // cout<<tag<<" "<<attribute<<endl;
    // find the tag => attribute from tag_mapping
    string attribute_line = tag_mapping[tag];
    // cout<<attribute_line<<endl;
    size_t equal_found = attribute_line.find('=');
    int start_index = 0;
    int is_found = 0;
    while (equal_found != string::npos) {
      int len = (equal_found - 1) - start_index;
      string key = attribute_line.substr(start_index, len);
      if (key == attribute) {
        is_found = 1;
        // get the attribute, print and break
        start_index = equal_found + 3;
        int end_index = attribute_line.find_first_of('"',start_index);
        string result = attribute_line.substr(start_index, end_index - start_index);
        cout<<result<<endl;
        break;
      }

      equal_found = attribute_line.find('=', equal_found + 1);
    }

    if (is_found == 0) {
      cout<<"Not Found!"<<endl;
    }
  }

  return 0;
}



// sample input
/*
10 10
<a value = "GoodVal">
<b value = "BadVal" size = "10">
</b>
<c height = "auto">
<d size = "3">
<e strength = "2">
</e>
</d>
</c>
</a>
a~value
b~value
a.b~size
a.b~value
a.b.c~height
a.c~height
a.d.e~strength
a.c.d.e~strength
d~sze
a.c.d~size


OUTPUT:
GoodVal
Not Found!
10
BadVal
Not Found!
auto
Not Found!
2
Not Found!
3
*/
