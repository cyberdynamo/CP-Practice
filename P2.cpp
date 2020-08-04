#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define endl '\n'
using namespace std;
int main()
{
 ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
 ll test;
 cin>>test;
 while(test--)
 {
     ll n;
     cin>>n;
     vector<ll> a(n),b(n);
     std::map<ll, ll> m1,m2,m3,m4,m5;

     for(ll i=0;i<n;i++)
        {
     cin>>a[i];
     m1[a[i]]+=1;
     m3[a[i]]+=1;
        }

     for(ll i=0;i<n;i++)
        {
     cin>>b[i];
     m2[b[i]]+=1;
     m3[b[i]]+=1;
        }

     ll f=0;
     for(auto i:m3)
     {
         if(i.second%2!=0)
         {
             f=1;
             break;
         }
     }

     ll t1[n],t2[n];
     for(ll i=0;i<n;i+=1)
     t1[i]=a[i];

     for(ll i=0;i<n;i+=1)
     t2[i]=b[i];

     sort(t1,t1+n);
     sort(t2,t2+n);

     ll p=0;
     for(ll i=0;i<n;i+=1)
     {
         if(t1[i]!=t2[i])
         {
             p=1;
             break;
         }
     }

     if(p==0)
     cout<<0<<endl;
     else if(f==1)
     cout<<-1<<endl;
     else
     {
     	ll c=0;
     	ll m=INT_MAX;
     	for(ll i=0;i<n;i+=1)
     	m=min(m,a[i]);
     	for(ll i=0;i<n;i+=1)
     	m=min(m,b[i]);
        for(auto i:m1)
        {
            if(i.second>m2[i.first])
            m4[i.first]=(i.second-m2[i.first])/2;
        }
        for(auto i:m2)
        {
            if(i.second>m1[i.first])
            m5[i.first]=(i.second-m1[i.first])/2;
        }
        std::vector<ll> v1,v2;
        for(auto i:m4)
        {
            for(ll j=0;j<i.second;j+=1)
            v1.pb(i.first);
        }
        for(auto i:m5)
        {
            for(ll j=0;j<i.second;j+=1)
            v2.pb(i.first);
        }

        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end(),greater<ll>());
        for(ll i=0;i<v1.size();i++)
        {
        	ll k1=v1[i];
        	ll k2=v2[i];
        	c+=min(2*m,(min(k1,k2)));
        }
        cout<<c<<endl;
     }
 }
 return 0;
}
