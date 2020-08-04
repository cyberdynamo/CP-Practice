#include "bits/stdc++.h"
using namespace std;using ll = long long;
inline void re(int& a){scanf("%d" , &a);};
int main()
{
    int n , c , k;
    re(n); re(c) ; re(k);
    int A[n];
    for(int i = 0; i < n; i++)
        re(A[i]);
    sort(A , A+n);
    int cnt = 1 , strt = 0;
    for(int i = 0; i < n; i++)
    {
        if((i-strt+1) <= c and ((A[i]-A[strt]) <= k))
            continue;
        else
            cnt++ , strt = i;
    }
    printf("%d\n", cnt);
}
