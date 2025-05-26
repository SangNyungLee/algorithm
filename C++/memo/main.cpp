// #include<bits/stdc++.h>
// using namespace std;

// int main(void){
// 	ios::sync_with_stdio(0);
// 	cin.tie(0);
// 	stack<pair<char, int>> st;
// 	string str;
// 	cin >> str;
// 	for(char c : str){
// 		// 여는 괄호일 경우에는 그냥 stack에 push해줌
// 		if (c == '(' || c == '[')
// 			st.push({c, -1});
// 		// 닫는 괄호일 경우
// 		else{
// 			// 숫자가 아니면
// 			char t = st.top().first;
// 			if (t != '#'){
// 				if (t == '['){
// 					st.pop();
// 					st.push({'#', 3});
// 				}
// 				else if (t == '('){
// 					st.pop();
// 					st.push({'#', 2});
// 				}
// 			}
// 			// first가 숫자면
// 			else{
// 				if (st.top().first == '#'){
// 					int tmp = 0;
// 					while(st.top().first == c){
// 						tmp += st.top().second * 3;
// 						st.pop();
// 					}
// 					st.pop();
// 					cout << tmp << "\n";
// 				}
// 			}
// 		}
// 	}
// }
#include <bits/stdc++.h>
using namespace std;

int main(void)
{
	cout << "hello world!";
}