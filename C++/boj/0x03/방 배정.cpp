#include <bits/stdc++.h>
using namespace std;

int a1[7] = {0}; // 남자
int a2[7] = {0}; // 여자
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N; // 참가하는 학생 수
	int K; // 한 방에 배정할 수 있는 최대 인원 수
	int res = 0;
	cin >> N >> K;
	for(int i = 0 ; i < N ; i++){
		int a, b;
		cin >> a >> b;
		if (a == 1) a1[b]++;
		else a2[b]++;
	}
	for(int i = 1 ; i < 7 ; i++){
		res += a1[i] / K;
		res += a2[i] / K;
		if (a1[i] % K) res++;
		if (a2[i] % K) res++;
		// if (a1[i] > K){
		// 	res += a1[i] / K;
		// 	if (a1[i] % K != 0) res++;
		// }
		// if (a2[i] > K){
		// 	res += a2[i] / K;
		// 	if (a2[i] % K != 0) res++;
		// }
	}
		
	cout << res << '\n';

}