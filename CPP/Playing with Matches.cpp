#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);

    ll t{};
    cin>>t;
    while(t--)
    {
        ll a{},b{};
        cin>>a>>b;
        ll d=a+b;
        string s=to_string(d);
        ll sum{};
        for(auto i:s)
        {
            if(i=='0')
                sum+=6;
            else if(i=='1')
                sum+=2;
            else if(i=='2')
                sum+=5;
            else if(i=='3')
                sum+=5;
            else if(i=='4')
                sum+=4;
            else if(i=='5')
                sum+=5;
            else if(i=='6')
                sum+=6;
            else if(i=='7')
                sum+=3;
            else if(i=='8')
                sum+=7;
            else if(i=='9')
                sum+=6;
        }
        cout<<sum<<endl;

    }


	return 0;
}

