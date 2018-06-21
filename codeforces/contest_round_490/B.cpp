//solved
#include<iostream>
using namespace std;

int main(){

    int n;
    cin>>n;
    string input;
    cin>>input;

    int divisor[n];
    divisor[0] = n;
    int divisorCount = 1;
    for(int i=n/2;i>0;i--){
        if(n%i == 0){
            divisor[divisorCount] = i;
            divisorCount++;
        }
    }


    for(int i=divisorCount-1;i>=0;i--){
        int l = 0;
        int r = divisor[i] - 1;
        if(l == r){
            continue;
        } else {
            //swap substring
            string newS = "";
            int newIndex = 0;
            for(int j=r;j>=0;j--){
                newS.insert(newIndex, 1, input[j]);
                newIndex++;
            }

            for(int k=newIndex;k<n;k++){
                newS.insert(k, 1, input[k]);
            }
            input = newS;
        }
    }

    cout<<input<<endl;

}
