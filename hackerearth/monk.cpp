//time limit exceeded

#include<iostream>

int CAPACITY;

class Node {
    public:
        Node(int index, int hashCode){
            this->index = index;
            this->hashCode = hashCode;
        }
        Node(){
            this->index = -1;
            this->hashCode = 0;
        }
    public:
        int index;
        int hashCode;
};

int getIndex(Node arr[],char ch){
    int hashIndex = (int) ch % CAPACITY;

     while(arr[hashIndex].hashCode != (int) ch){
            hashIndex++;
            hashIndex = hashIndex % CAPACITY;
    }

    return arr[hashIndex].index;

}

int main(){

    std::string str = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    CAPACITY = str.length();
    Node arr[CAPACITY];

    for(int i=0;i<CAPACITY;i++){
        int hashIndex = (int) str[i] % CAPACITY;

        while(arr[hashIndex].index != -1){
            hashIndex++;
            hashIndex = hashIndex%CAPACITY;
        }

        if(arr[hashIndex].index == -1){
            Node node(i,(int) str[i]);
            arr[hashIndex] = node;
        }
    }

    //take input
    int T;
    std::cin>>T;
    for(int i=0;i<T;i++){
        std::string strList[20];
        int si = 0;
        do{
            std::cin>>strList[si];
            si++;
        } while((std::cin.get() != '\n'));

        int sum = 0;
        for(int i=0;i<si;i++){
            for(int j=0;j<strList[i].length();j++){
                sum += j + getIndex(arr,strList[i][j]);
            }
        }
        std::cout<<sum*si<<std::endl;

    }
}

