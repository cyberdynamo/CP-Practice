#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	ll t{};
	cin>>t;
	while(t--)
    {
        ll n,k;
        cin>>n>>k;
        for(ll i=0;i<n;i++)
        {
            ll m{};
            cin>>m;
            if(m%k==0)
                cout<<1;
            else
                cout<<0;
        }
        cout<<endl;
    }

	return 0;
}
