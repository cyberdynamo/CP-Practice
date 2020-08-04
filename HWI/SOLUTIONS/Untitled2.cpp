#include "bits/stdc++.h"
using namespace std;using ll = long long;
inline void re(int& a){scanf("%d" , &a);};
const ll MOD = 1e9 + 7;
int main(){
    int n,m; re(n) , re(m);
    vector<string> bits(n);
    int p[n] , mask[n];
    for(int i= 0 ; i <n; i++){
        re(p[i]) , cin>>bits[i];
        mask[i] = stoi(bits[i],0,2);
    }
    ll ans[m+1] = {0};
    for(int i =1;i < 1ll<<n; i++){
        ll costh = 1ll ;
        int maskh = (1ll<<m) -1;
        for(int j =0;j<n; j++){
            if(i>>j&1){
                costh = (costh*p[j])%MOD , maskh &= mask[j];
            }
        }
        int u = __builtin_popcount(maskh);
        ans[u] = (ans[u] + costh)%MOD;
    }
    for(int i = 0; i<=m; i++)
        printf("%lld ",ans[i]);
    printf("\n");
}
