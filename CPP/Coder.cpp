#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int n{};
    cin>>n;
    if(n%2==0)
        cout<<(n/2)*n<<endl;
    else
        cout<<((n/2)+1)*((n/2)+1)+((n/2)*(n/2))<<endl;
     ll p=1;
     ll q=1;
    for(int i=0;i<n;i++)
    {
        if(p==1)
            q=1;
        else
            q=-1;
        p*=-1;
        for(int j=0;j<n;j++)
        {
            if(q==1)
                cout<<"C";
            else
                cout<<".";
            q*=-1;
        }
        cout<<endl;
    }



	return 0;
}
