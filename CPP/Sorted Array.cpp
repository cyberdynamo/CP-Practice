#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ll n;
    cin>>n;

    vector<ll> v{};
    for(ll i=0;i<n;i++)
    {
        ll m{};
        cin>>m;
        v.pb(m);
    }
    int flag=0;
    for(ll i=1;i<n;i++)
    {
        if(v.at(i-1)>v.at(i))
           {
               cout<<"false"<<endl;
               flag=1;
               break;
           }
    }
    if(flag==0)
        cout<<"true"<<endl;

	return 0;
}

