#include<bits/stdc++.h>
using namespace std;

#define MAXN 222
#define sd(x) scanf("%d",&x)
#define ll long long int
#define MOD 100000LL

int a[MAXN];
ll dp[MAXN][MAXN];

ll ways(int l, int r)
{
    ll ret;
    if(a[l] == -1){
        if(a[r] == -1){
            ret = 3;
        }
        else{
            if(a[r] % 2 == 0){
                ret = 1;
            }
            else{
                ret = 0;
            }
        }
    }
    else{
        if(a[l] % 2 == 1){
            if(a[r] == -1){
                ret = 1;
            }
            else{
                if(a[r] == a[l] + 1){
                    ret = 1;
                }
                else{
                    ret = 0;
                }
            }
        }
        else{
            ret = 0;
        }
    }
    //cout<<l<<" "<<r<<" "<<a[l]<<" "<<a[r]<<" "<<ret<<endl;
    return ret;
}

ll f(int l, int r){
    if(dp[l][r] != -1){
        return dp[l][r];
    }
    ll &ret = dp[l][r];
    cout<<&ret<<endl;
    if(l > r){
        return ret = 1;
    }
    ret = 0;
    for(int k = l + 1; k <= r; k++){
        ret += (ways(l, k) * f(l + 1, k - 1) * f(k + 1, r));
        ret %= MOD;
    }
    //cout<<ways(l,r)<<endl;
    //cout<<l<<" "<<r<<" "<<ret<<endl;
    return ret;
}

int main(){
    int n;
    string s;
    sd(n);
    cin>>s;
    for(int i = 0; i < n; i++){
        if(s[i] == 'A'){
            a[i] = 1;
        }
        else if(s[i] == 'a'){
            a[i] = 2;
        }
        else if(s[i] == 'B'){
            a[i] = 5;
        }
        else if(s[i] == 'b'){
            a[i] = 6;
        }
        else if(s[i] == 'C'){
            a[i] = 9;
        }
        else if(s[i] == 'c'){
            a[i] = 10;
        }
        else{
            a[i] = -1;
        }
    }
    memset(dp, -1, sizeof(dp));
    cout<<f(0, n - 1)<<endl;
    return 0;
}