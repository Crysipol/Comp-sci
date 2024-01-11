//Name: Kevin Paute
//Email: Kevin.paute88@myhunter.cuny.edu

#include <iostream>
using namespace std;

main()
{
    int year, time;
    float p;
    p = 325.7;
    year = 2017;

    cout << "Please enter number of years: ";
    cin >> time; 
    int i, change;
    cout << "Year " << year << p << endl;

    for (i = 1; i < time; i++)
    {
        year = year + 1;
        p = p + ((12.4/1000) * p) - ( (8.4/1000) * p);
        cout << "Year " << year << " " << p << endl;
    }
}