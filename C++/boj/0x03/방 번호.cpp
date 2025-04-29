#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	int arr[9] = {};
	while(N > 0){
		if (N % 10 == 9) arr[6]++;
		else arr[N%10]++;
		N /= 10;
	}
	if (arr[6] % 2 != 0) arr[6] += 1;
	arr[6] /= 2;
	int res = 0;
	for(int i = 0 ; i < 9 ; i++){
		res = max(res, arr[i]);
	}
	cout << res;
}