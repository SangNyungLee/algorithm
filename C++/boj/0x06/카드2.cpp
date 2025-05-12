#include <bits/stdc++.h>
using namespace std;

int N;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N;
	queue<int> q;
	for(int i = 1 ; i <= N ; i++)
		q.push(i);
	while(q.size() > 1){
		int t;
		q.pop();
		t = q.front();
		q.pop();
		q.push(t);
	}
	cout << q.front() << '\n';
}