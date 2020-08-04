#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll sum=0;
    ll q;
    while(true)
    {
        cin>>q;
        sum+=q;
        if(sum<0)
            break;
        cout<<q<<endl;
    }

	return 0;
}

