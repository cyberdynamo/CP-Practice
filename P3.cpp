#include<bits/stdc++.h>
#define ll long long int
#define endl '\n'
using namespace std;

int main()
{
ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
 ll t;
 cin>>t;
 while(t--)
 {
    ll n,x;
    cin>>n>>x;

    vector<ll> v(n);
    for(ll& i:v)
    cin>>i;
    sort(v.begin(),v.end());
    vector<ll>::iterator it = lower_bound(v.begin(), v.end(), x);
    ll lb = it - v.begin();
    ll d=0;
    for(ll i=lb;i<n;i++)
    {
    	if(x<v[i])
    	{
    		while(x<v[i])
    		{
    			x=2*x;
    			d++;
    		}
    		d++;
    	}
    	else
    	d++;
    	x=2*v[i];
    }
    ll tot=lb+d;
    if(lb!=0)
    {
    	d=0;
    	lb--;
    	for(ll i=lb;i<n;i++)
    	{
    		if(x<v[i])
    		{
    			while(x<v[i])
    			{
    				x=2*x;
    				d++;
    			}
    			d++;
    		}
    		else
    		d++;
    		x=2*v[i];
    	}
    	ll ans=min(d+lb,tot);
    	cout<<ans<<endl;
    }
    else
    cout<<tot<<endl;
 }
 return 0;
}
