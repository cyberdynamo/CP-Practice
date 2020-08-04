#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;
    while(n--)
    {
        string s;
        cin>>s;
        ll l = s.size();
        cout<<""<<endl;
        for(ll i=0;i<l;i++)
        {
            for(ll j=i;j<l;j++)
            {
                cout<<s.substr(i,j-i+1)<<endl;
            }
        }
    }
	return 0;
}
