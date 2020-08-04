#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;
    cout<<1<<endl;
    n--;

    for(ll i=1;i<=n;i++)
    {
        cout<<i;
        for(ll j=1;j<=i-1;j++)
            cout<<0;
        cout<<i<<endl;
    }

	return 0;
}
