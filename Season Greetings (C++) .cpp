//Name: Kevin Paute
//Email: Kevin.paute88@myhunter.cuny.edu

#include <iostream>
using namespace std;

int main ()
{
    int a;
    cout << "Enter month (as a Number):";
    cin >> a;
    if ((a < 3) or (a > 11))
    {
        cout << "Happy Winter";
    }
    else if ((3 <= a) and (a < 7))
    {
        cout << "Happy Spring\n";
    }
    else if ((7 <= a) and (a < 9))
    {
        cout << "Happy Summer\n";
    }
    else 
    {
        cout << "Happy Fall\n";
    }

    
}
