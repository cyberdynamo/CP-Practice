/*
░█████╗░██╗░░░██╗██████╗░███████╗██████╗░██████╗░██╗░░░██╗███╗░░██╗░█████╗░███╗░░░███╗░█████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝████╗░██║██╔══██╗████╗░████║██╔══██╗
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝██║░░██║░╚████╔╝░██╔██╗██║███████║██╔████╔██║██║░░██║
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║░░╚██╔╝░░██║╚████║██╔══██║██║╚██╔╝██║██║░░██║
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║██████╔╝░░░██║░░░██║░╚███║██║░░██║██║░╚═╝░██║╚█████╔╝
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░
*/

#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pb push_back
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    ll n{};
    cin>>n;
    string s{};
    cin>>s;

    ll arr[26]={};
    for(ll i=0;i<s.size();i++)
    {
        if(isupper(s[i])!=0)
        {
        ll temp{};
        temp=int(s[i]);
        arr[temp-65]+=1;
        }
        else
        {
            ll temp{};
            temp=int(s[i]);
            arr[temp-97]+=1;
        }
    }

    int flag=0;
    for(ll i=0;i<26;i++)
        if(arr[i]==0)
    {
        cout<<"NO"<<endl;
        flag=1;
        break;
    }

    if(flag==0)
        cout<<"YES"<<endl;


	return 0;
}
