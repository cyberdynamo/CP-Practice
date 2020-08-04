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
        ll num;
        cin>>num;
        ll s1{},s2{};
        while(num)
        {
            ll d=num%10;
            if(d%2==0)
                s1+=d;
            else
                s2+=d;
            num=int(num/10);
        }
        if(s1%4==0 || s2%3==0)
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }

	return 0;
}
