#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ll t{};
    cin>>t;
    while(t--)
    {
        ll k{};
        cin>>k;

        ll m{};
        if(k%8!=0)
            m=k%8;
        else
            m=8;

        ll l=k/8;

        cout<<"O";
        ll i{};
        if(k<=8)
            for(i=1;i<=k-1;i++)
                cout<<".";
        else
            for(i=1;i<=7;i++)
                cout<<".";

        for(;i<=7;i++)
            cout<<"X";
        cout<<endl;

        ll q{};
        if(k%8==0)
        {
            q=k/8;
            q--;
        }
        else
            q=k/8;
        q--;
        for(ll z=1;z<=q;z++)
        {
            for(ll y=1;y<=8;y++)
                cout<<".";
            cout<<endl;
        }

        if(k>8)
        {
            ll j{};
            for(j=1;j<=m;j++)
                cout<<".";
            for(ll k=1;k<=(8-m);k++)
                cout<<"X";
            cout<<endl;
        }

        for(ll a=1;a<(8-k/8);a++)
        {
            for(ll b=1;b<=8;b++)
                cout<<"X";
            cout<<endl;
        }
        if(k%8==0 && k!=64)
            cout<<"XXXXXXXX"<<endl;

    }
	return 0;
}
