#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;
    if(n==1)
	{
        ll a;
		cin>>a;
		cout<<a<<endl;
	}
    else if(n==2)
    {
        ll a,b;
        cin>>a>>b;
        cout<<__gcd(a,b);
    }
    else
    {
        ll a,b;
        cin>>a>>b;
        ll g=__gcd(a,b);
        for(ll i=1;i<=n-2;i++)
        {
            ll c;
            cin>>c;
            g=__gcd(g,c);
        }
        cout<<g<<endl;
    }

	return 0;
}
