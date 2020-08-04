#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ll t{};
    cin>>t;
    while(t--)
    {
        ll a{},b{},n{};
        cin>>a>>b>>n;
        ll d=min(a,b);
        ll e=max(a,b);
        ll count=0;
        while(1)
        {
            if(d>n)
                break;
            d+=e;
            d,e=e,d;
            count+=1;
        }
        cout<<count<<endl;
    }


	return 0;
}

