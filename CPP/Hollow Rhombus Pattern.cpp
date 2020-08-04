#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    int n;
    cin>>n;

    for(ll i=1;i<n;i++)
        cout<<" ";
    for(ll i=1;i<=n;i++)
        cout<<"*";
    cout<<endl;

    for(ll i=n-2;i>0;i--)
    {
        for(ll j=1;j<=i;j++)
            cout<<" ";
        cout<<"*";
        for(ll j=1;j<=n-2;j++)
            cout<<" ";
        cout<<"*"<<endl;
    }

    for(ll i=1;i<=n;i++)
        cout<<"*";
    cout<<endl;

	return 0;
}
