#include<iostream>
#include<vector>
#include<cmath>
//#include<iomanip>
#include<cstdio>
using namespace std;

double getDistance(double,double,double,double);
int main(){

    vector<double>Xcor;
    vector<double>Ycor;
    double x,y;

    int test;
    cin>>test;
    for(int i=0;i<test;i++){
        cin>>x>>y;
        Xcor.push_back(x);
        Ycor.push_back(y);
    }


    //calculation
    int maxDistance=0;
    int x1,x2,y1,y2;
    for(int i=0;i<test;i++){
        x1=Xcor[i];
        y1=Ycor[i];
        for(int j=i+1;j<test;j++){
            x2=Xcor[j];
            y2=Xcor[j];

            double distance=getDistance(x1,x2,y1,y2);
            if(distance>maxDistance){
                maxDistance=distance;

            }
        }
    }
    cout<<maxDistance<<endl;

}

//distance between two cordinates
double getDistance(double x1,double x2,double y1,double y2){
    double x12=pow(x1-x2,2);
    double y12=pow(y1-y2,2);
    double distance=sqrt(x12+y12);
    return distance;
}


