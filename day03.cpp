//SOLVED DAY 03 of 30 days of Code

#include<iostream>
#include<cmath>
using namespace std;

int main(){
    double mealCost,totalCost,tipCost,taxCost;
    int tipPercent,taxPercent;
    cin>>mealCost>>tipPercent>>taxPercent;

    //calculation
    tipCost=mealCost*((double)tipPercent/100);
    taxCost=mealCost*((double)taxPercent/100);

    //output
    totalCost=round(mealCost+tipCost+taxCost);
    cout<<"The total meal cost is "<<totalCost<<" dollars."<<endl;

    return 0;
}
