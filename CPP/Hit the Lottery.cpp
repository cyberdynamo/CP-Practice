#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    ll n{};
    cin>>n;
    ll s=0;
    s+=n/100;
    n=n%100;
    s+=n/20;
    n=n%20;
    s+=n/10;
    n=n%10;
    s+=n/5;
    n=n%5;
    s+=n/1;
    cout<<s<<endl;

	return 0;
}

