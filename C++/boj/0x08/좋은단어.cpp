#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, res = 0;
	cin >> N;
	cin.ignore();
	while(N--){
		stack<char> st;
		string str;
		getline(cin, str);
		for(char c : str){
			if (!st.empty() && st.top() == c) st.pop(); 
			else st.push(c);
		}
		if (st.empty()) res++;
	}
	cout << res << '\n';
}