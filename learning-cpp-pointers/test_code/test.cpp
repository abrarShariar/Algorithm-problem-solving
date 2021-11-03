#include<iostream>
using namespace std;


class Car {
    public:
        int power;
        string name;

        Car() {};

        Car(int power, string name) {
            this->power = power;
            this->name = name;
        }
};


void printAllCarNames(Car *car) {
    for (int i = 0; i < 3; i++) {
        cout << (car+i)->name << endl;
    }
}

void modifyAllCarNames (Car *car) {
    for (int i = 0; i < 3; i++) {
       (car+i)->name = (car+i)->name + "ZZZ";
    }
}


int main() {
//    string newUser = "Michael";
//    string *userName = &newUser;
//
//    cout << userName <<endl;
//    cout << *userName <<endl;
//
//    *userName = "Abrar";
//
//    cout << userName << endl;
//    cout << newUser << endl;
//    cout << *userName <<endl;
//    cout << &newUser <<endl;
//
//    delete userName;
//    cout << *userName << endl;
//    cout << newUser << endl;

// Arrays
//    int myNumbers[10] = { 99,2,3 };
//    int *pMyNumber = myNumbers;
//
//    cout << pMyNumber <<endl;
//    cout << myNumbers <<endl;
//
//    while (*pMyNumber) {
//        cout << *pMyNumber <<endl;
//        pMyNumber++;
//    }
//
//
//    for (int i = 0; i < sizeof(myNumbers)/sizeof(myNumbers[0]); i++) {
//        cout << "Address of element: " << i << " : " << pMyNumber + i << endl;
//        cout << "Value: " << *(pMyNumber + i) << endl;
//    }
//
//    for (int i = 0; i < sizeof(myNumbers)/sizeof(myNumbers[0]); i++) {
//        cout << *pMyNumber->i <<endl;
//    }


    // Pointers of pointers
    Car *c1;
    Car *c2;
    Car *c3;

    c1 = new Car(1, "BMW");
    c2 = new Car(2, "Toyota");
    c3 = new Car(3, "Merc");
    Car* carPool[3] = {c1, c2, c3};

    printAllCarNames(*carPool);
    modifyAllCarNames(*carPool);
    printAllCarNames(*carPool);

//
//    cout << carPool[0]->name <<endl;
//    cout << carPool[0] <<endl;


//    for (int i = 0; i < sizeof(carNames)/sizeof(carNames[0]); i++) {
//        c1 = new Car(i, carNames[i]);
//        carPool[i] = c1;
//    }

    // Loop over each item in car pool
//    for (int i = 0; i < sizeof(carPool)/ sizeof(carPool[i]); i++) {
//        cout << **(carPool[i]) << endl;
//    }

    // Loop over with a pointer of pointer
//    Car **ppCar = carPool;
//    while (ppCar) {
//        cout << **(ppCar <<endl;
//        ppCar++;
//    }


    // Dynamic memoery location
}




