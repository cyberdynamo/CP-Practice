#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ll n;
    cin>>n;

    ll arr[n];
    for(ll i=0;i<n;i++)
        cin>>arr[i];

    reverse(arr,arr+n);

    for(ll i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<"END"<<endl;

	return 0;
}
