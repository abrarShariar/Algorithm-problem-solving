#include<iostream>
using namespace std;

struct Student{
    int age;
    string first_name;
    string last_name;
    int standard;
};

int main(){
    Student s1;
    cin>>s1.age>>s1.first_name>>s1.last_name>>s1.standard;
    cout<<s1.age<<" "<<s1.first_name<<" "<<s1.last_name<<" "<<s1.standard<<endl;

}
