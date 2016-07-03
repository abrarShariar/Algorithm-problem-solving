//SOLVED
//30DaysOfCode

#include<iostream>
using namespace std;

int makeHourGlass(int *hArr);

int main(){
    int MAX;
   int arr[6][6];

   for(int i=0;i<6;i++){
    for(int j=0;j<6;j++){
        int num;
        cin>>num;
        arr[i][j]=num;
    }
   }

    int resArr[16];
    int k=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            int *parr=&arr[i][j];
            int calcMax=makeHourGlass(parr);
            resArr[k]=calcMax;
            k++;
        }
    }

    MAX=resArr[0];
    for(int i=0;i<16;i++){
        int checkNum=resArr[i];
        if(checkNum>MAX){
            MAX=checkNum;
        }
    }
    cout<<MAX<<endl;

    //makeHourGlass(&arr[0][0]);
}

int makeHourGlass(int *hArr){

    int sum=0;
    for(int i=0;i<3;i++){
        //cout<<*(hArr+i)<<" ";
        sum+=*(hArr+i);
    }
    //cout<<endl;
    //cout<<"  "<<*(hArr+7)<<" "<<endl;
    sum+=*(hArr+7);
    for(int i=12;i<15;i++){
        //cout<<*(hArr+i)<<" ";
        sum+=*(hArr+i);
    }

    return sum;
}
