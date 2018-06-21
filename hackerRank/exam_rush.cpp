//SOLVED:
#include<iostream>
#include<algorithm>

using namespace std;

int main(){

    int totalChapter, hoursLeft;
    cin>>totalChapter>>hoursLeft;


    int arr[totalChapter];
    for(int i=0;i<totalChapter;i++){
        cin>>arr[i];
    }

    sort(arr, arr+totalChapter);

    int chapterCount = 0, index = 0;
    while(hoursLeft >= 0){
        if(arr[index] <= hoursLeft){
            chapterCount++;
            hoursLeft = hoursLeft - arr[index];
        } else {
            break;
        }
        index++;
    }

    cout<<chapterCount<<endl;

    //test print
    //print(arr, totalChapter);
}
