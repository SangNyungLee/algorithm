#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	while(T--){
		deque<string> dq;
		string str;
		string str2;
		int n;
		bool rev = true;
		bool check = true;
		cin >> str >> n >> str2;
		string str3 = "";
		for(char c : str2){
			if (c == '[' || c == ']')
				continue;
			else if (c == ','){
				dq.push_back(str3);
				str3="";
			}
			else str3 += c;
		}
		if (str3 != "")
			dq.push_back(str3);
		for(char c : str){
			if (c == 'R')
				rev = !rev;
			else if (c == 'D'){
				if (dq.empty()){
					cout << "error" << '\n';
					check = false;
					break;
				}
				else{
					if (rev)
						dq.pop_front();
					else
						dq.pop_back();
				}
			}
		}
		if (dq.empty() && check){
			cout << "[]\n";
		}
		else if (rev && check){
			cout << "[";
			while(!dq.empty()){
				if (dq.size() > 1){
					cout << dq.front() << ",";
					dq.pop_front();
				}
				else{
					cout << dq.front() << "]\n";
					dq.pop_front();
				}
			}
		}
		else if (!rev && check){
			cout << "[";
			while(!dq.empty()){
				if (dq.size() > 1){
					cout << dq.back() << ",";
					dq.pop_back();
				}
				else{
					cout << dq.back() << "]\n";
					dq.pop_back();
				}
			}
		}
	}
}