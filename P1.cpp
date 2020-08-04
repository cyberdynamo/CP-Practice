#include<bits/stdc++.h>
using namespace std;
main(){
	int t;
	cin>>t;
	while(t--){
		int k;
		cin>>k;
		char a[8][8];

		int count = 1;
		for(int i=0; i<8; i++){
			for(int j=0; j<8; j++){
				if(i == 0 && j == 0){
					a[i][j] = 'O';
				}
				else if(count < k){
					a[i][j] = '.';
					count++;
				}
				else{
					a[i][j] = 'X';
				}
			}
		}

		for(int i=0; i<8; i++){
			for(int j=0; j<8; j++)
			   cout<<a[i][j]<<" ";
			cout<<"\n";
		}
	}
}
