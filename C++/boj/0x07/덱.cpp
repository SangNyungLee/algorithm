#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
	cin.tie(0);
	deque<int> queue;
	int N;
	cin >> N;
	
	while(N--){
		string str;
		cin >> str;
		if (str == "push_back"){
			int x;
			cin >> x;
			queue.push_back(x);
		}
		else if (str == "push_front"){
			int x;
			cin >> x;
			queue.push_front(x);
		}
		else if (str == "pop_front"){
			if (queue.empty())
				cout << -1 << '\n';
			else{
				cout << queue.front() << '\n';
				queue.pop_front();
			}
		}
		else if (str == "pop_back"){
			if (queue.empty())
				cout << -1 << '\n';
			else{
				cout << queue.back() << '\n';
				queue.pop_back();
			}
		}
		else if (str == "size"){
			cout << queue.size() << '\n';
		}
		else if (str == "empty"){
			cout << queue.empty() << '\n';
		}
		else if (str == "front"){
			if (queue.empty())
				cout << -1 << '\n';
			else
				cout << queue.front() << '\n';
		}
		else if (str == "back"){
			if (queue.empty())
				cout << -1 << '\n';
			else
				cout << queue.back() << '\n';
		}
	}
}