#include <iostream>
using namespace std;
int main()
{
    long long n, a[200000], i, j,m=55555555555, s=0, b,k,p=0;
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> a[i];
        if (a[i] <=m)
        {
            m = a[i];
            k = i;
        }
        {
            if (a[i]<a[i-1] && i!=0)
            { p=1;}
    }
    for (i = k; i < n - 1; i++)
    {
        if (a[i+ 1] < a[i])
        {
            s = 1;
            break;
        }
    }
    m = a[n - 1];
    for (i = 0; i < k - 1; i++)
    {
        if (a[i] < m || a[i + 1] < a[i])
        {
            s = 1;
            break;
        }
    }
    if (s == 1)
        cout << "-1";
    else
    {if (k==0 || p==1)k=n;
        cout<<n-k;
}
}//1 3 2 4

