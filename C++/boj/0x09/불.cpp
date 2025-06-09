#include <bits/stdc++.h>
using namespace std;

int graph[1001][1001];
int visited[1001][1001];
int T, w, h;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    while (T--)
    {
        bool flag = false;
        cin >> w >> h;
        queue<pair<int, int>> Q;
        queue<pair<int, int>> fire;
        for (int i = 0; i < 1001; i++)
        {
            fill(graph[i], graph[i] + 1000, 0);
            fill(visited[i], visited[i] + 1000, 0);
        }
        for (int i = 0; i < h; i++)
        {
            string str;
            cin >> str;
            for (int j = 0; j < w; j++)
            {
                graph[i][j] = str[j];
                if (str[j] == '@')
                {
                    Q.push({i, j});
                    visited[i][j] = 1;
                }
                else if (str[j] == '*')
                    fire.push({i, j});
            }
        }
        while (!Q.empty())
        {
            int f_size = fire.size();
            while (f_size--)
            {
                auto [x, y] = fire.front();
                fire.pop();
                for (int i = 0; i < 4; i++)
                {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (nx < 0 || ny < 0 || nx >= h || ny >= w)
                        continue;
                    if ((graph[nx][ny] != '#' || graph[nx][ny] != '*') && graph[nx][ny] == '.')
                    {
                        graph[nx][ny] = '*';
                        fire.push({nx, ny});
                    }
                }
            }
            int q_size = Q.size();
            while (q_size--)
            {
                auto [x, y] = Q.front();
                Q.pop();
                for (int i = 0; i < 4; i++)
                {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (nx < 0 || ny < 0 || nx >= h || ny >= w)
                    {
                        if (!flag)
                        {
                            cout << visited[x][y] << '\n';
                            flag = true;
                        }
                        continue;
                    }
                    if (graph[nx][ny] == '#' || graph[nx][ny] == '*' || visited[nx][ny] != 0)
                        continue;
                    if (graph[nx][ny] == '.')
                    {
                        visited[nx][ny] = visited[x][y] + 1;
                        Q.push({nx, ny});
                    }
                }
            }
        }
        if (!flag)
            cout << "IMPOSSIBLE\n";
    }
}