#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll t{};
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        reverse(s.begin(),s.end());
        ll result=0;
        ll var=0;
        for(auto i:s)
        {
            result+=((int(i)-48)*pow(2,var));
            var++;
        }
        cout<<result<<endl;
    }

	return 0;
}

