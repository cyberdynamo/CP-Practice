#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int main()
{
    string s;
    cin>>s;

    for(ll i=0;i<s.size();i++)
    {
        if(i==0 && s[i]=='9')
            continue;
        if (int(s[i])-48>4)
            s.at(i)=char((9-(int(s[i])-48))+48);
    }
    cout<<s<<endl;

	return 0;
}

