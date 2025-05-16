#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	string str;
	while(1){
		stack<char> st;
		// 한 줄을 공백 포함해서 통째로 입력 받으려면 getline을 사용하면됨
		getline(cin, str); 
		bool flag = true;
		if (str == ".")
			return (0);
		for(char c : str){
			if (st.empty() && c == '.'){
				cout << "yes" << '\n';
				break;
			}
			else if (!st.empty() && c == '.'){
				cout << "no" << '\n';
				flag = false;
			}
			if (c == '(' || c == '[')
				st.push(c);
			if (c == ')' || c == ']'){
				if (!st.empty() && c == ')' && st.top() == '(')
					st.pop();
				else if (!st.empty() && c == ']' && st.top() == '[')
					st.pop();
				else
					flag = false;
			if (!flag){
				cout << "no" << '\n';
				break;
			}
			}
		}
	}
}