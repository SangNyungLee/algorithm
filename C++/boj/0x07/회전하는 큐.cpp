#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	deque<int> queue;
	int N, M, i = 0;
	int res = 0;
	cin >> N >> M;
	while(N--)
		queue.push_front(N + 1);

	while(M--){
		int x;
		cin >> x;
		int tmp = 0;
		int len = queue.size();
		while(queue.front() != x){
			queue.push_back(queue.front());
			queue.pop_front();
			tmp++;
		}
		queue.pop_front();
		res += min(len - tmp, tmp);
	}
	cout << res;
}
// 특정 위치에 있는 값을 queue에서 찾으려면 find 함수 사용하면 됨
// int idx = find(queue.begin(), queue.end(), t) - queue.begin();
// 이렇게 하면 t가 있는 위치를 찾을 수 있음