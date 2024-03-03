//Name: Kevin Paute
//Email: Kevin.paute88@myhunter.cuny.edu

#include <iostream>
using namespace std;

int main()
{
    int year;
    cout << "Enter year: "; cin >> year;
    while (year > 2018)
    {
        cout << "Year must be 2018 or earlier" << endl;
        cout << "Enter year: ";
        cin >> year;
    }
    cout << "You entered: " << year << endl;

}
