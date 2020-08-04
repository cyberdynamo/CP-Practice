#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
    ll n{};
    cin>>n;
    if(n>=1 and n<=50)
        cout<<100<<endl;
    else if(n>=51 and n<=100)
        cout<<50<<endl;
    else
        cout<<0<<endl;


	return 0;
}

