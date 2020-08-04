#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;

    for(ll i=1;i<=n;i++)
    {
        if(i%2!=0)
        {
                for(ll j=1;j<=i;j++)
                {
                cout<<1;
                }
                cout<<endl;
        }
        else
        {
            cout<<1;
            for(ll j=1;j<=i-2;j++)
                cout<<0;
            cout<<1<<endl;
        }
    }

	return 0;
}
