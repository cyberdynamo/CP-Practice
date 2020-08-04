#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;

    for(ll i=0;i<n;i++)
    {
        for(ll j=0;j<=i;j++)
            cout<<"*";
        cout<<endl;
    }

	return 0;
}

