#include <bits/stdc++.h>
using namespace std;

int graph[1002][1002];
int visited[1002][1002] = {0};
int R, C;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> R >> C;
    queue<pair<int, int>> Q;
    queue<pair<int, int>> fire;

    // graph에 값 넣기
    for (int i = 0; i < R; i++)
    {
        string str;
        cin >> str;
        for (int j = 0; j < C; j++)
        {
            graph[i][j] = str[j];
            if (str[j] == 'J')
            {
                Q.push({i, j});
                visited[i][j] = 1;
            }
            else if (str[j] == 'F')
                fire.push({i, j});
        }
    }

    while (!Q.empty())
    {
        int f_size = fire.size();
        // 불 먼저 움직이기
        while (f_size--)
        {
            auto [x, y] = fire.front();
            fire.pop();
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= R || ny >= C)
                    continue;
                // 불이 움직일 때 같은 불이나 벽이 아닐 때 퍼짐
                if (graph[nx][ny] == '.' || graph[nx][ny] == 'J')
                {
                    graph[nx][ny] = 'F'; // 불이 번졌으니깐 바꿔줌
                    fire.push({nx, ny});
                }
            }
        }
        // 불 이동 후 지훈이가 움직이기
        int q_size = Q.size();
        while (q_size--)
        {
            auto [x, y] = Q.front();
            Q.pop();
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= R || ny >= C)
                {
                    cout << visited[x][y] << '\n';
                    return (0);
                }
                // 갈 수 잇는 길이고 방문하지 않았을 때
                if (graph[nx][ny] == '.' && !visited[nx][ny])
                {
                    visited[nx][ny] = visited[x][y] + 1;
                    Q.push({nx, ny});
                }
            }
        }
    }
    cout << "IMPOSSIBLE" << '\n';
}