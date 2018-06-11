#include<iostream>
using namespace std;

//merge subroutine
void Merge(char* s, int l, int m, int r){
    int n1 = (m-l)+1;
    int n2 = r-m;

    string lSt;
    string rSt;

    for(int i=0;i<n1;i++){
        lSt[i] = s[l+i];
    }

    for(int i=0;i<n2;i++){
        rSt[i] = s[m+1+i];
    }

    int li=0,ri=0,ki=l;
    while(li<n1 && ri<n2){
        if(lSt[li] <= rSt[ri]){
            s[ki] = lSt[li];
            li++;
        } else {
            s[ki] = rSt[ri];
            ri++;
        }
        ki++;
    }

    while(li<n1){
        s[ki] = lSt[li];
        li++;
        ki++;
    }

     while(ri<n2){
        s[ki] = rSt[ri];
        ri++;
        ki++;
    }
}

void mergeSort(char* c, int l, int r){
    if(l < r){
        int mid = (l+r)/2;
        mergeSort(c,l,mid);
        mergeSort(c,mid+1,r);
        Merge(c,l,mid,r);
    }
}


int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        char* s2;
        char* s1;
        cin>>s1;
        cin>>s2;

        mergeSort(s1,0, (sizeof(s1)/sizeof(s1[0])) -1);
        //mergeSort(s2,0, s1.length()-1);

        cout<<s1<<" "<<s2<<endl;
    }





}
