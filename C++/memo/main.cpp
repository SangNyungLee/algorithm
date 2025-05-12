#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<int> st;
	int N;
	int MAX = 0;
	cin >> N;
	int res = N;
	while(N--){
		int x;
		cin >> x;
		if (st.empty()){
			st.push(x);
			continue;
		}
		if (!st.empty() && x > st.top()){
			while(!st.empty() && x > st.top())
				st.pop();
			st.push(x);
			res++;
		}
		else
			st.push(x);
	}
	cout << res;
}