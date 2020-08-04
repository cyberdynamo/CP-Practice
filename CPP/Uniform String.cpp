#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    ll n{},m{};
    cin>>n>>m;

    ll k=n%10;
    ll a=1;
    while(1)
    {
        ll z=k*a;
        a+=1;
        ll q=z%10;
        if(q==0)
        {
            cout<<a-1<<endl;
            break;
        }
        if(q==m)
        {
            cout<<a-1<<endl;
            break;
        }
    }


	return 0;
}
