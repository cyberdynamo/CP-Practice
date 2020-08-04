#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n,x,y;
    cin>>n>>x>>y;
    ll count=0;
    ll f1{},f2{},f3{},f4{};
    while(n--)
    {
        ll p,q;
        cin>>p>>q;
        if(p!=x && q!=y)
        {
            if(f1==0 && p-q==0)
            {
                count++;
                f1=1;
            }
            else if(f2==0 && p+q==0)
            {
                count++;
                f2=1;
            }
        }

        else if(p==x && q!=y)
        {
            if(f3==0)
            {
                count++;
                f3=1;
            }
        }

        else if(q==y && p!=x)
        {
            if(f4==0)
            {
                count++;
                f4=1;
            }
        }
        else
            count++;
    }
    cout<<count<<endl;

	return 0;
}
