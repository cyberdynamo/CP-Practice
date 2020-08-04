#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    ll n;
    cin>>n;
    while(n--)
    {
        string s;
        cin>>s;
        string r{};
        ll i{};
        for(i=0;i<s.size()-1;i++)
        {
            if(s.at(i)=='p' && s.at(i+1)=='i')
            {
                r+="3.14";
                i++;
            }
            else
                r+=s.at(i);
        }

        if(i==s.size()-1)
            r+=s.at(s.size()-1);
        cout<<r<<endl;
    }

	return 0;
}
