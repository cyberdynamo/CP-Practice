#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n{};
    cin>>n;

    for(ll i=1;i<=2*(n-1)+1;i++)
        cout<<'*';
    cout<<endl;

    ll q=n;
    ll w=1;
    for(ll i=1;i<n;i++)
    {
        for(ll j=1;j<=q-1;j++)
        {
            cout<<'*';
        }

        for(ll j=1;j<=w;j++)
            cout<<" ";
        w+=2;

        for(ll j=1;j<=q-1;j++)
        {
            cout<<'*';
        }
        cout<<endl;
        q-=1;
    }


    q=2;
    w=2*n-5;
     for(ll i=1;i<n-1;i++)
    {
        for(ll j=1;j<=q;j++)
        {
            cout<<'*';
        }

        for(ll j=1;j<=w;j++)
            cout<<" ";
        w-=2;

        for(ll j=1;j<=q;j++)
        {
            cout<<'*';
        }
        cout<<endl;
        q+=1;
    }

    for(ll i=1;i<=2*(n-1)+1;i++)
        cout<<'*';
    cout<<endl;


	return 0;
}

