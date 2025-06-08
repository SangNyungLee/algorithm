#include <bits/stdc++.h>
using namespace std;

int dx[8] = {2, 2, 1, 1, -1, -1, -2, -2};
int dy[8] = {1, -1, 2, -2, 2, -2, 1, -1};
int graph[301][301];
int visited[301][301];
int N, T, a, b;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    while (T--)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
        {
            fill(graph[i], graph[i] + N, 0);
            fill(visited[i], visited[i] + N, -1);
        }
        queue<pair<int, int>> Q;
        int x1, y1, x2, y2;
        // x1,y1 : 나이트가 있는 칸
        // x2,y2 : 나이트가 가려고 하는 칸
        cin >> x1 >> y1 >> x2 >> y2;
        // 둘의 좌표가 같으면 바로 다음으로 넘어감
        if (x1 == x2 && y1 == y2)
        {
            cout << 0 << '\n';
            continue;
        }
        Q.push({x1, y1});
        visited[x1][y1] = 0;
        while (!Q.empty())
        {
            auto [x, y] = Q.front();
            Q.pop();
            for (int i = 0; i < 8; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= N || ny >= N)
                    continue;
                if (visited[nx][ny] == -1)
                {
                    Q.push({nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        cout << visited[x2][y2] << '\n';
    }
}