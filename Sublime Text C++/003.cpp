#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll n{};
    cin>>n;
    ll arr[n];
    for(ll i{};i<n;i++)
        cin>>arr[i];
    sort(arr,arr+n);
    for(ll j=0;j<n;j++)
        cout<<arr[j]<<" ";
}
