#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
ll factorial(ll n)
{
    if(n==0 || n==1)
        return 1;
    else
        return n*factorial(n-1);
}
int main()
{
    ll n;
    cin>>n;
    ll sum{};
    for(ll i=0;i<n;i++)
    {
        ll q;
        cin>>q;
        sum+=(factorial(q));
    }
    cout<<(sum%107)<<endl;
	return 0;
}

