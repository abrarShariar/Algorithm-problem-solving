
//time limit excedded
#include<iostream>
using namespace std;

int main(){

    int hashArr[27];
    for(int i=0;i<27;i++){
        hashArr[i] = 0;
    }
    int n,k;
    cin>>n>>k;

    char input[n];
    for(int i=0;i<n;i++){
        cin>>input[i];
        int key = (int) input[i] - 97;
        hashArr[key] = hashArr[key] + 1;
    }

    int delCount = 0;
    int startIndex = 0;
    while(delCount < k && startIndex < 27){
        if(hashArr[startIndex] > 0) {
            char ch = (char) (startIndex + 97);
            for(int i=0;i<n;i++){
                if(input[i] == ch){
                    input[i] = '0';
                    delCount++;
                    hashArr[startIndex] = hashArr[startIndex] - 1;
                    break;
                }
            }
        } else {
            startIndex++;
        }
    }

    for(int i=0;i<n;i++){
        if(input[i] != '0'){
            cout<<input[i];
        }
    }

}
