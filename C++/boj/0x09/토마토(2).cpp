#include <bits/stdc++.h>
using namespace std;

int M, N, H;
int graph[101][101][101];
int visited[101][101][101];
int dx[6] = {-1, 1, 0, 0, 0, 0};
int dy[6] = {0, 0, -1, 1, 0, 0};
int dz[6] = {0, 0, 0, 0, -1, 1};
queue<tuple<int, int, int>> Q;
bool flag = false;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N >> H;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < M; k++)
            {
                cin >> graph[i][j][k];
                if (graph[i][j][k] == 0)
                {
                    flag = true;
                    visited[i][j][k] = -1;
                }
                if (graph[i][j][k] == 1)
                {
                    Q.push({i, j, k});
                    visited[i][j][k] = 0;
                }
            }
    if (!flag)
    {
        cout << 0;
        return (0);
    }
    while (!Q.empty())
    {
        auto [x, y, z] = Q.front();
        Q.pop();
        for (int i = 0; i < 6; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            int nz = z + dz[i];

            if (nx < 0 || ny < 0 || nz < 0 || nx >= H || ny >= N || nz >= M)
                continue;
            if ((visited[nx][ny][nz] == -1 && graph[nx][ny][nz] == 0))
            {
                Q.push({nx, ny, nz});
                visited[nx][ny][nz] = visited[x][y][z] + 1;
            }
        }
    }

    int res = 0;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < M; k++)
            {
                if (visited[i][j][k] == -1 && graph[i][j][k] == 0)
                {
                    cout << -1;
                    return (0);
                }
                if (visited[i][j][k] > res)
                    res = visited[i][j][k];
            }
    cout << res;
    // cout << '\n';
    // for (int i = 0; i < H; i++)
    // 	for (int j = 0; j < N; j++)
    // 	{
    // 		for (int k = 0; k < M; k++)
    // 		{
    // 			cout << visited[i][j][k] << ' ';
    // 		}
    // 		cout << '\n';
    // 	}
}