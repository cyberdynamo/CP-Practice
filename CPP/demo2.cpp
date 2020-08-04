#include <iostream>
#include <cctype>
using namespace std;
int main()
{
    char x;
    cin >> x;
    if (islower(x))
        cout << "Lowercase";
    else
        cout << "Not Lowercase.";

    return 0;
}
