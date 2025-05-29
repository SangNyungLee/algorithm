#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int M, N;
int graph[1001][1001];
bool visited[1001][1001] = {false};
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    int MAX = 0;
    queue<pair<int, int>> queue;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            cin >> graph[i][j];
            if (graph[i][j] == 1)
            {
                visited[i][j] = true;
                queue.push({i, j});
            }
        }

    while (!queue.empty())
    {
        pair<int, int> cur = queue.front();
        queue.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M)
                continue;
            if (!visited[nx][ny] && !graph[nx][ny])
            {
                queue.push({nx, ny});
                visited[nx][ny] = true;
                graph[nx][ny] = graph[cur.first][cur.second] + 1;
                if (graph[nx][ny] > MAX)
                    MAX = graph[nx][ny];
            }
        }
    }
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (graph[i][j] == 0)
                MAX = -1;
    if (MAX == -1 || MAX == 0)
        cout << MAX;
    else
        cout << MAX - 1;
}