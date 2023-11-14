#include <string>
#include <iostream>
using namespace std;

int pik(void) {
    int test = 123;
    return 0;
};  


class testClass {
    public:
        int testNum;
        string testStr;
};

class users {
    public:
        int age;
        string firstName;
        string lastName;
        string homeAdress;
};

int main() {
    testClass testObj;
    testObj.testNum = 69;
    testObj.testStr = "Hello, World!";

    cout << testObj.testNum;
    cout << "\n";
    cout << testObj.testStr;
    cout << "\n";
    cout << "\n";

    
    users user1;
    user1.age = 17;
    user1.firstName = "Jeppe";
    user1.lastName = "Bøgeskov";
    user1.homeAdress = "Alpeviolvej 3";

    users user2;
    user2.age = 16;


    cout << user1.age;
    cout << "\n";
    cout << user1.firstName + " " + user1.lastName;
    cout << "\n";
    cout << user1.homeAdress;
    cout << "\n";
    cout << "\n";
    cout << user2.age;
    cout << "\n";
    cout << "\n";
    cout << "\n";
    
    for (size_t i = 0; i < user1.firstName.length(); i++)
    {
        cout << "test";
    }
    
    return 0; 
}   