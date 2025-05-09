#include <bits/stdc++.h>
using namespace std;
const int MX = 1000005;
int s[MX];
int pos = 0;

void push(int val){
	s[pos++] = val;
}
void pop(){
	pos--;
}
int top(){
	return s[pos - 1];
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	while (N--){
		string str;
		cin >> str;
		if (str == "push"){
			int x;
			cin >> x;
			push(x);
		}
		else if (str == "pop"){
			if (pos == 0) cout << "-1" << '\n';
			else{
				cout << s[pos - 1] << '\n';
				pop();	
			}
		}
		else if (str == "size"){
			cout << pos << '\n';
		}
		else if (str == "empty"){
			if (pos == 0) cout << "1" << '\n';
			else cout << "0" << '\n';
		}
		else if (str == "top"){
			if (pos == 0) cout << "-1" << '\n';
			else cout << s[pos - 1] << '\n';
		}
	}
 }

 /*
 
 */