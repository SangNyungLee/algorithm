#include <bits/stdc++.h>
using namespace std;

int graph[101][101];    // 일반 사람
bool visited[101][101]; // 일반사람
int graph2[101][101];   // 적록색약인 사람
bool visited2[101][101];
int N;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};
int pos;
void bfs(int a, int b)
{
    queue<pair<int, int>> Q;
    Q.push({a, b});
    pos = graph[a][b];
    visited[a][b] = true;
    while (!Q.empty())
    {
        auto [x, y] = Q.front();
        Q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= N || ny >= N)
                continue;
            if (!visited[nx][ny] && graph[nx][ny] == pos)
            {
                visited[nx][ny] = true;
                Q.push({nx, ny});
            }
        }
    }
}
void bfs2(int a, int b)
{
    queue<pair<int, int>> Q;
    Q.push({a, b});
    pos = graph2[a][b];
    visited[a][b] = true;
    while (!Q.empty())
    {
        auto [x, y] = Q.front();
        Q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= N || ny >= N)
                continue;
            if (!visited[nx][ny] && graph2[nx][ny] == pos)
            {
                visited[nx][ny] = true;
                Q.push({nx, ny});
            }
        }
    }
}
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    int res = 0;
    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;
        for (int j = 0; j < N; j++)
        {
            graph[i][j] = str[j];
            if (str[j] == 'R')
                graph2[i][j] = 'G';
            else
                graph2[i][j] = str[j];
        }
    }
    // 일반
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (!visited[i][j])
            {
                bfs(i, j);
                res++;
            }
    cout << res << ' ';
    for (int i = 0; i < N; i++)
        fill(visited[i], visited[i] + N, false);
    res = 0;
    // 색약
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (!visited[i][j])
            {
                bfs2(i, j);
                res++;
            }
    cout << res;
}