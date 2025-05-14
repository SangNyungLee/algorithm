#include <bits/stdc++.h>
using namespace std;

int main(void){
	deque<int> dq;
	dq.push_front(10);
	dq.push_back(50);
	dq.push_front(24);
	for(auto x : dq) cout << x;
	cout << dq.size() << '\n';
	if(dq.empty()) cout << "DQ is empty\n";
	else cout << "DQ is not empty\n";
	dq.pop_front();
	dq.pop_back();

	cout << dq.back() << '\n';
	dq.push_back(72);
	cout << dq.front() << '\n';
	dq.push_back(12);
	dq[2] = 17;
	dq.insert(dq.begin() + 1, 33);
	dq.insert(dq.begin() + 4, 60);
	for(auto x : dq) cout << x << ' ';
	cout << '\n';
	dq.erase(dq.begin() + 3);
	cout << dq[3] << '\n';
	dq.clear();
}