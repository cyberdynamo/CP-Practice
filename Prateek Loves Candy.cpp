#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
bool isprime(ll n)
{
    if(n==0)
        return false;
    else if(n==1)
        return false;
    else if(n==2)
        return true;
    else
    {

		for(ll i=2;i<int(sqrt(n))+1;i++)
        {
            if(n%i==0)
                return false;
        }
        return true;
    }
}
int main()
{
    ll const num=1000001;
    ll arr[num]{};
    ll j=0;
    for(ll i=2;i<num;i++)
    {
        if(isprime(i)==true)
        {
            arr[j]=i;
            j++;
        }
    }

    ll t;
    cin>>t;

    while(t--)
    {
        ll n;
        cin>>n;
        cout<<arr[n-1]<<endl;
    }

	return 0;
}

