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
        ll a{},b{},c{},n{};
        cin>>a>>b>>c>>n;
        if(n==0 and a==b and b==c)
            cout<<"YES"<<endl;
        else
            {
        ll arr[]={a,b,c};
        sort(arr,arr+3);
        ll s{};
        s+=arr[2]-arr[0];
        s+=arr[2]-arr[1];
        n=n-s;
        if(n<0)
            cout<<"NO"<<endl;
        else if(n%3==0)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
            }
    }


	return 0;
}

