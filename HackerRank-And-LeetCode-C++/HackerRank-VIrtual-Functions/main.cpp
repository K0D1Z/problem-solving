//
// Created by kzatorski on 4/29/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person {
public:
    string name;
    int age;

    virtual void getdata() = 0;
    virtual void putdata() = 0;
    virtual ~Person() = default;
};

class Professor : public Person {
public:
    int publications, cur_id;
    static int counter;

    Professor() {
        counter++;
        cur_id = counter;
    }

    ~Professor() = default;

    void getdata() override {
        cin >> name;
        cin >> age;
        cin >> publications;
    }

    void putdata() override {
        cout << name << " " << age << " " << publications << " " << cur_id << endl;
    }
};

class Student : public Person {
public:
    vector<int> marks;
    int cur_id;
    static int counter;

    Student() {
        counter++;
        cur_id = counter;
    }
    ~Student() = default;

    void getdata() override {
        cin >> name;
        cin >> age;
        int temp;
        for (int i = 0; i < 6; i++) {
            cin >> temp;
            marks.push_back(temp);
        }
    }
    void putdata() override {
        int sum_of_elems = 0;
        for(std::vector<int>::iterator it = marks.begin(); it != marks.end(); ++it)
        {
           sum_of_elems += *it;
        }
        cout << name << " " << age << " " << sum_of_elems << " " << cur_id << endl;
    }
};

int Student::counter = 0;
int Professor::counter = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
