#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    string s;
    cin>>s;
    string v{};
    for(ll i=0;i<s.size();i++)
    {
        if(s.at(i)=='0')
            v+='5';
        else
            v+=s[i];
    }
    cout<<v<<endl;
	return 0;
}

