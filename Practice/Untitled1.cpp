// C++ Program to find n'th fibonacci Number
#include<iostream>
#include<cmath>
using namespace std;
int fib(int n) {
double phi = (1 + sqrt(5)) / 2;
return (pow(phi, n) / sqrt(5));
}

// Driver Code
int main ()
{
    while(true){
int n;
std::cin>>n;
std::cout << fib(n) << std::endl;
    }
return 0;
}
//This code is contributed by Lokesh Mohanty.

