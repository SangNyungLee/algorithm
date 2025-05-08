#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	/*
	'-' : 백스페이스, 커서의 앞에 글자가 존재하면 그 글자를 지워버림
	'>', '<' : 화살표, 커서 +1, -1
	나머지는 그대로 입력 받으면 된다.
	*/
	int L;
	cin >> L;
	while(L--){
		string str;
		cin >> str;
		list<char> lst;
		auto pos = lst.begin();
		for(char c : str){
			if (c == '<'){
				if (pos != lst.begin()) 
					pos--;
			}
			else if (c == '>'){
				if (pos != lst.end()) 
					pos++;
			}
			else if (c == '-'){
				if (pos != lst.begin()){
					pos--;
					pos = lst.erase(pos);
				}
			}
			else{
				lst.insert(pos, c);
			}
		}
		for(auto t : lst) cout << t;
		cout << '\n';
	}

}