#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;
    ll m=n;
    if(n%2!=0)
    {
    while(n>=1)
    {
        cout<<n<<endl;
        n--;n--;
    }

    ll c=2;
    while(c<=m-1)
    {
        cout<<c<<endl;
        c++;c++;
    }
    }

    else
    {
        n-=1;
        while(n>=1)
        {
            cout<<n<<endl;
            n--;n--;
        }

        ll c=2;
        while(c<=m)
        {
            cout<<c<<endl;
            c++;c++;
        }
    }

	return 0;
}
