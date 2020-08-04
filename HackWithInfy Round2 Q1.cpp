#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll T;
    cin>>T;

    while(T--)
    {
        ll N;
        cin>>N;

        ll arr[N+1]={0}, DP[N+1]={0}, Bad[N+1]={0};
        for(ll i=0;i<N;i++)
            cin>>arr[i];
        arr[N]=1e9;

        for(ll i=0;i<N;i++)
            cin>>Bad[i];

        for(ll i=N-1;i>=0;i--)
        {
            if(arr[i+1]>arr[i])
                DP[i]=DP[i+1]+1;
            else
                DP[i]=1;
        }


        //for(ll j=0;j<N;j++)
        //    cout<<DP[j]<<endl;
        ll sum=0;
        for(ll i=0;i<N;i++)
        {
            if(Bad[i]!=1)
                sum+=DP[i];
        }
        cout<<sum<<endl;
    }

    return 0;
}
