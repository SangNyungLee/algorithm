#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	long long res = 0;
	cin >> N;
	stack<int> st;

	while(N--){
		int x;
		cin >> x;
		if (st.empty()){
			st.push(x);
			continue;
		}
		while (!st.empty() && x >= st.top())
			st.pop();
		res += st.size();
		st.push(x);
	}
	cout << res;
}