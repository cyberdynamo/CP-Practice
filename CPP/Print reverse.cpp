#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n{};
    cin>>n;
    ll m=n;
    ll count=0;
    while(m)
    {
        m/=10;
        count++;
    }
    count--;
    ll sum{};

    while(n)
    {
        ll d=n%10;
        sum+=d*(pow(10,count));
        n/=10;
        count--;
    }
    cout<<sum<<endl;

	return 0;
}
