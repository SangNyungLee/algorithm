#include <iostream>
#include <utility>
#include <queue>
using namespace std;

int graph[502][502];
bool visited[502][502] = {false};
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int N, M;
int bfs(int x, int y){
	queue<pair<int, int>> queue;
	visited[x][y] = true;
	queue.push({x,y});
	int res = 1;
	while(!queue.empty()){
		pair<int, int> cur = queue.front();
		queue.pop();
		for(int i = 0 ; i < 4 ; i++){
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
			if (visited[nx][ny] || graph[nx][ny] == 0) continue;
			visited[nx][ny] = true;
			queue.push({nx,ny});
			res++;
		}
	}
	return res;
}
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;
	int cnt = 0;
	int area = 0;
	for(int i = 0 ; i < N ; i++)
		for(int j = 0 ; j < M ; j++)
			cin >> graph[i][j];
	for(int i = 0 ; i < N ; i++)
		for(int j = 0 ; j < M ; j++){
			if (!visited[i][j] && graph[i][j] == 1){
				int tmp = bfs(i,j);
				cnt++;
				if (tmp > area)
					area = tmp;
			}
		}
	cout << cnt << '\n' << area;
}