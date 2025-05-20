#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	string str;
	int res = 0;
	stack<char> st;
	cin >> str;

	for(int i = 0 ; i < str.length() ; i++){
		if (str[i] == '(') st.push(str[i]);
		else{
			if (str[i - 1] == '('){ // 레이저일 경우
				st.pop();
				res += st.size();
			}
			else{
				st.pop();
				res++;
			}
 		}
	}
	cout << res << "\n";
}

// #include<bits/stdc++.h>
// using namespace std;

// int main(void){
// 	ios::sync_with_stdio(0);
// 	cin.tie(0);
// 	string str;
// 	int res = 0;
// 	stack<char> st;
// 	cin >> str;

// 	for(char c : str){
// 		if (c == '(') st.push(c);
// 		else{
// 			st.pop();
// 			res += st.size();	
// 		}
// 	}
// 	cout << res << '\n';
// }