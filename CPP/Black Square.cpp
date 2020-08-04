#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ll a{},b{},c{},d{};
    cin>>a>>b>>c>>d;
    string s;
    cin>>s;
    ll sum{};
    for(auto i:s)
    {
        if(i=='1')
            sum+=a;
        else if(i=='2')
            sum+=b;
        else if(i=='3')
            sum+=c;
        else
            sum+=d;
    }
    cout<<sum<<endl;

	return 0;
}
