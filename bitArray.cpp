#include<iostream>
#include<vector>

int main(){

    std::vector<int> numList;
    int N,S,P,Q;
    std::cin>>N>>S>>P>>Q;

    numList.push_back(S);
    for(int i=1;i<N;i++){
        int inNum=((numList[i-1]*P)+Q);
        bool isDistinct=true;
        for(int j=0;j<numList.size();j++){
            if(inNum==numList[j]){
                isDistinct=false;
                break;
            }
        }
        if(isDistinct){
            numList.push_back(inNum);
        }
    }

    std::cout<<numList.size()<<std::endl;
}

    //------------------------CALCULATION
    /*

    for(std::vector<int>::iterator it=numList.begin();it!=numList.end();++it){
        int checkNum=*it;
        bool isDistinct=true;

        for(std::vector<int>::iterator it2=it+1;it2!=numList.end(); ){
            if(checkNum==*it2){
                isDistinct=false;
                it2=numList.erase(it2);
            }else{
                ++it2;
            }
        }
        /*
        if(isDistinct){
            resList.push_back(checkNum);
        }
       */
        //RESULT
    //std::cout<<numList.size()<<std::endl;
    //test output
    /*
    std::cout<<"ResList: "<<std::endl;
   for(std::vector<int>::iterator it=resList.begin();it!=resList.end();++it){
        std::cout<<*it<<std::endl;
    }
    */
