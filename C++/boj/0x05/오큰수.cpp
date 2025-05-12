#include <bits/stdc++.h>
using namespace std;

int arr[1000001];

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<pair<int, int>> st;
	int N, M;
	cin >> N;
	M = N;
	int i = 1;
	while(N--){
		int x;
		cin >> x;
		if (st.empty()){
			st.push({x, 0});
			continue;
		}
		while(!st.empty() && x > st.top().first){
			// 새로 들어온 애가 기존 것 보다 크면
			arr[st.top().second] = x;
			st.pop();
		}
		st.push({x, i++});
	}
	while (!st.empty()){
		arr[st.top().second] = -1;
		st.pop();
	}
	for(int k = 0 ; k < M ; k++){
		cout << arr[k] << ' ';
	}
}