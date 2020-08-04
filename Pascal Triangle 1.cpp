#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;

    if(n==0)
        cout<<"";
    else if(n==1)
        cout<<1<<endl;
    else if(n==2)
    {
        cout<<" "<<1<<endl;
        cout<<1<<" "<<1<<endl;
    }
    else
    {
        ll arr[10][10]{};
        arr[0][0]=1;
        arr[1][0]=1;
        arr[1][1]=1;

        for(ll i=2;i<n;i++)
        {
            arr[i][0]=1;
            arr[i][i]=1;

            for(ll k=1;k<i;k++)
            {
                arr[i][k]=arr[i-1][k-1]+arr[i-1][k];
            }
        }

        ll q=n-1;
        for(ll i=0;i<n;i++)
        {
            cout<<" ";
            for(ll k=1;k<=q;k++)
                cout<<" ";

            q--;

            for(ll j=0;j<=i;j++)
                cout<<arr[i][j]<<" ";
            cout<<endl;
        }

    }

	return 0;
}

