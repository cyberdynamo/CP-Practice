#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll a,b,c;
    cin>>a>>b>>c;

    ll d;
    d=pow(b,2)-4*a*c;

    ll x,y;
    x=((-b)+sqrt(pow(b,2)-4*a*c))/2*a;
    y=((-b)-sqrt(pow(b,2)-4*a*c))/2*a;

    if(d<0)
    {
        cout<<"Imaginary"<<endl;
    }
    else if(d>0)
    {
        cout<<"Real and Distinct"<<endl;
        if(x>y)
            cout<<int(y)<<" "<<int(x)<<endl;
        else
            cout<<int(x)<<" "<<int(y)<<endl;
    }
    else
    {
        cout<<"Real and Equal"<<endl;
        cout<<int(x)<<" "<<int(y)<<endl;
    }

	return 0;
}

