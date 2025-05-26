#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int graph[102][102];
bool visited[102][102];
int n,m;
string str;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void dfs(int x, int y){
	queue<pair<int, int>> queue;
	queue.push({x,y});
	visited[x][y] = true;
	while(!queue.empty()){
		pair<int, int> cur = queue.front();
		queue.pop();
		for(int dir = 0 ; dir < 4 ; dir++){
			int nx = cur.first + dx[dir];
			int ny = cur.second + dy[dir];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if (visited[nx][ny] || !graph[nx][ny] == 1) continue;
			queue.push({nx,ny});
			visited[nx][ny] = 1;
			graph[nx][ny] = graph[cur.first][cur.second] + 1;
		}
	}
}
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	for(int i = 0 ; i < n ; i++){
		string str;
		cin >> str;
		for(int j = 0 ; j < m ; j++){
			graph[i][j] = str[j] - '0';
		}
	}
	dfs(0,0);
	cout << graph[n - 1][m - 1];
}