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
        ll n{},m{};
        cin>>n>>m;
        ll k=n%m;
        if(k==0)
            cout<<0<<endl;
        else
            cout<<m-k<<endl;
    }


	return 0;
}

