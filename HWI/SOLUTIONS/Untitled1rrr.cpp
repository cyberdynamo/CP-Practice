#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	ll t{};
	cin>>t;
	while(t--)
    {
        ll n,m,x,y;
        cin>>n>>m>>x>>y;
        if(n==1 && m==1)
        {
            cout<<x<<endl;
            continue;
        }
        if(2*x<=y)
        {
            cout<<n*m*x<<endl;
        }
        else
        {
            ll flag=0;
        if(m%2!=0)
            flag=1;
        if(flag==0)
        {
            ll sum=0;
            for(ll i=0;i<n;i++)
            {
                sum+=m/2;
            }
            cout<<sum*y<<endl;
        }
        else
        {
            ll pairs=0;
            ll count1=0;
            ll count2=0;
            for(ll i=0;i<n;i++)
            {
                if(i%2==0)
                {
                    pairs+=m/2;
                    count1++;
                }
                else
                {
                    pairs+=m/2;
                    count2+=1;
                }
            }
            if(y>x)
            {
                cout<<pairs*y+count1*x+count2*(y-x)<<endl;
            }
            else
            {
                cout<<pairs*y+count1*y<<endl;
            }
        }
        }
    }

	return 0;
}
