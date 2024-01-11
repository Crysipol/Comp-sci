//Name: Kevin Paute
//Email: Kevin.paute88@myhunter.cuny.edu

#include <iostream>
using namespace std;

main()
{
    int n, x;
    cout << "Enter a number: "; 
    cin >> n;
    if (n< 0)
    {
        cout << "1";
        x = 32 + n;
    }
    else if (n >= 0)
    {
        cout << "0";
        x = n;
    }
    int b;
    b = 16;
    while (b > 0.5)
    {
        if (x >= b)
        {
            cout << "1";
        }
        else
        {
            cout << "0";     
        }
        x = x % b;
        b = b / 2;
    }
    cout << '\n';
}