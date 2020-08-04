#include<iostream>
#define ll long long
using namespace std;
int main()
{
    int a[5]={1,2,3,4,5};
    int b[5]={8,9,1,2,5};

    int c[50]={};
    int t{};

    for(int i=0;i<5;i++)
    {
        for(int j=0;j<b[i];j++)
        {
            c[t]=a[i];
            t++;
        }
    }

    for(int i=0;i<50;i++)
        cout<<c[i]<<" ";
}

