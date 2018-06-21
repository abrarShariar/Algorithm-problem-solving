//time limit exceeded
#include<iostream>

int main(){

    int n,k;
    std::cin>>n>>k;

    std::string input;
    std::cin>>input;

    char start = 'a';
    int counter = 0;
    int startIndex = 0;

    while(start <= 'z' && counter < k){
        std::size_t found = input.find(start);
        if(found != std::string::npos){
            //found
            input.erase(found,1);
            counter++;
        } else {
            start++;
        }
    }

    std::cout<<input<<std::endl;
}
