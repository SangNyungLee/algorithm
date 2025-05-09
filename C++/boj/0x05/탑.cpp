#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	stack<pair<int, int>> st;
	int arr[500001] = {};
	for(int i = 1 ; i <= N ; i++){
		int x;
		cin >> x;
		if (i == 1){
			arr[1] = 0;
			st.push({x,i}); // 값, 인덱스 순서로 넣어둠
			continue;
		}
		// x > top
		if (x > st.top().first){
			// 앞으로 가면서 나보다 큰 애를 찾고, 작은애들은 다 부셔버림
			while(st.empty() == false){
				if (st.top().first <= x)
					st.pop();
				else{
					arr[i] = st.top().second;
					break;
				}
			}
		}
		// top > x
		else
			arr[i] = st.top().second;
		st.push({x,i});
	}
	for(int i = 1 ; i <= N ; i++)
		cout << arr[i] << ' ';
}