#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    ll t{};
    cin>>t;
    while(t--)
    {
        ll a{},b{};
        cin>>a>>b;
        if(a%2==0 or b%2==0)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }


	return 0;
}

