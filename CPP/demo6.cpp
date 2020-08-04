#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    ll a{},b{};
    char c{};
    cin>>a>>b>>c;
    if(c=='+')
        cout<<a+b<<endl;
    else if(c=='-')
        cout<<a-b<<endl;
    else if(c=='*')
        cout<<a*b<<endl;
    else
        cout<<fixed<<setprecision(6)<<(float)a/b<<endl;
	return 0;
}

