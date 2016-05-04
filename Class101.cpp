//solved
#include<iostream>
#include<string>
#include<sstream>
using namespace std;

class Student{
private:
    int age;
    string first_name;
    string last_name;
    int standard;

public:
    //setters
    void set_age(int age);
    void set_first_name(string first_name);
    void set_last_name(string last_name);
    void set_standard(int standard);
    //getters
    int get_age();
    string get_first_name();
    string get_last_name();
    int get_standard();
    //method
    string to_string();
};

//setters
void Student::set_age(int age){
    this->age=age;
}
void Student::set_first_name(string first_name){
    this->first_name=first_name;
}
void Student::set_last_name(string last_name){
    this->last_name=last_name;
}
void Student::set_standard(int standard){
    this->standard=standard;
}
//getters
int Student::get_age(){
    return this->age;
}
string Student::get_first_name(){
    return this->first_name;
}
string Student::get_last_name(){
    return this->last_name;
}
int Student::get_standard(){
    return this->standard;
}

string Student::to_string(){
    //conversion of int to string
    int num=this->get_age();
    string strAge;
    ostringstream convert;
    convert<<num;
    strAge=convert.str();

    convert.str(string());

    num=this->get_standard();
    string strStandard;
    convert<<num;
    strStandard=convert.str();

    string text=strAge+","+this->get_first_name()+","+this->get_last_name()+","+strStandard;
    return text;

}


int main() {
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}

