// C++ Program to find n'th fibonacci Number
#include<iostream>
#include<cmath>
using namespace std;
int fib(int n) {
double phi = (1 + sqrt(5)) / 2;
return int(pow(phi, n) / sqrt(5));
}

// Driver Code
int main ()
{
    while(true)
    {
int n;
cin>>n;
for(int i=0;i<n;i++)
std::cout << fib(i) <<" ";
    }
return 0;
}
//This code is contributed by Lokesh Mohanty.
