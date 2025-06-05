#include <bits/stdc++.h>
using namespace std;
int T, M, N, K;
// 지역 변수로 선언하면 segmentation fault 뜨니까 밖에 선언하고 안에서 초기화 해주는게 좋음
int graph[2501][2501];
bool visited[2501][2501];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void bfs(int a, int b)
{
    queue<pair<int, int>> Q;
    Q.push({a, b});
    visited[a][b] = true;
    graph[a][b] = 0;
    while (!Q.empty())
    {
        auto [x, y] = Q.front();
        Q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= M || ny >= N)
                continue;
            if (!visited[nx][ny] && graph[nx][ny])
            {
                visited[nx][ny] = true;
                graph[nx][ny] = 0;
                Q.push({nx, ny});
            }
        }
    }
}
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    while (T--)
    {
        cin >> M >> N >> K;
        queue<pair<int, int>> Q;
        int res = 0;
        // 새로 선언하지 말고 초기화 해주는게 더 좋음
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                graph[i][j] = 0;
                visited[i][j] = false;
            }
        }
        while (K--)
        {
            int x, y;
            cin >> x >> y;
            graph[x][y] = 1;
        }
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (graph[i][j])
                {
                    bfs(i, j);
                    res++;
                }
            }
        }
        cout << res << '\n';
    }
}