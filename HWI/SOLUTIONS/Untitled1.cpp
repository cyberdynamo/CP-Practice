#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define ff first
#define ss second

map<ll,vector<ll> > a,b;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	ll t;
	cin>>t;
	while(t--)
	{
	    ll n,m,x,y,g,h;
	    cin>>m>>n;
	    for(ll i=0;i<m;i++)
	    {
	        cin>>x>>y;
	        a[x].pb(y);
	    }
	    for(ll i=0;i<m;i++)
	    {
	        cin>>x>>y;
	        b[x].pb(y);
	    }
	    cin>>g>>h;
	    ll cgood=0,cgreat=0;
	    for(auto it:a)
	    {
	        ll i=0,j=0;
	        x=it.ff;
	        cgood+=min(a[x].size(),b[x].size());
	        sort(a[x].begin(),a[x].end());
	        sort(b[x].begin(),b[x].end());
	        for(ll j=0;j<b[x].size();j++)
	        {
	            if(b[x][j]<=a[x][i])
	            {
	                if(b[x][j]==a[x][i])
	                {
	                    cgreat++;
	                    j++;
	                    i++;
	                    continue;
	                }
	                if(j+1<b[x].size())
	                {
	                    if(b[x][j+1]<=a[x][i])
	                        continue;
	                    else
	                        i++;
	                }
	            }
	        }
	    }

	    if(cgreat>=h && cgood>=g)
	        cout<<"Great\n";
	    else if(cgood>=g)
	        cout<<"Good\n";
	    else
	        cout<<":(\n";
	}
	return 0;
}
