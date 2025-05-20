#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	while(N--){
		stack<char> st;
		string str;
		cin >> str;
		bool flag = true;
		for(char c : str){
			if (c == '(') st.push(c);
			else if (!st.empty() && c == ')' && st.top() == '(')
				st.pop();
			else
				flag = false;
		}
		if (!flag || !st.empty()) cout << "NO" << '\n';
		else cout << "YES" << '\n';
	}
}