#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int graph[101][101];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
deque<int> dq;
int bfs(int a, int b)
{
	queue<pair<int, int>> Q;
	Q.push({a, b});
	int area = 1;
	while (!Q.empty())
	{
		auto [x, y] = Q.front();
		Q.pop();
		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || ny < 0 || nx >= N || ny >= M || graph[nx][ny] == 1)
				continue;
			if (graph[nx][ny] == 0)
			{
				Q.push({nx, ny});
				graph[nx][ny] = 1;
				area++;
			}
		}
	}
	return area;
}
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M >> K;
	int res = 0;
	while (K--)
	{
		int x1, x2, y1, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int i = min(y1, y2); i < max(y1, y2); i++)
		{
			for (int j = min(x1, x2); j < max(x1, x2); j++)
				graph[i][j] = 1;
		}
	}
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (graph[i][j] == 0)
			{
				res++;
				dq.push_back(bfs(i, j));
			}
		}
	}
	cout << res << '\n';
	sort(dq.begin(), dq.end());
	while (!dq.empty())
	{
		int front = dq.front();
		dq.pop_front();
		cout << front << ' ';
	}
}