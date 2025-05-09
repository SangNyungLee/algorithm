#include <bits/stdc++.h>
using namespace std;

int N;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N;
	stack<int> st, pu;
	string res;
	for(int i = N ; i > 0 ; i--)
		st.push(i);
	while(N--){
		int x;
		cin >> x;
		while (!st.empty() && st.top() <= x){
			pu.push(st.top());
			st.pop();
			res += "+\n";
		}
		if (!pu.empty() && pu.top() == x){
			pu.pop();
			res += "-\n";
		}
		else{
			cout << "NO" << '\n';
			return (0);
		}
	}
	cout << res;
 }