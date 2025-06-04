#include <bits/stdc++.h>
using namespace std;

bool graph[100001] = {false};
int N, K;
int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> K;
    if (N == K)
    {
        cout << 0 << '\n';
        return (0);
    }
    queue<pair<int, int>> Q;
    Q.push({N, 0});
    while (!Q.empty())
    {
        auto [x, y] = Q.front();
        Q.pop();
        for (int i = 0; i < 3; i++)
        {
            int nx = x;
            if (i == 0)
                nx -= 1;
            else if (i == 1)
                nx += 1;
            else
                nx *= 2;
            if (nx < 0 || nx > 100001)
                continue;
            if (nx == K)
            {
                cout << y + 1 << '\n';
                return (0);
            }
            if (!graph[nx])
            {
                graph[nx] = true;
                Q.push({nx, y + 1});
            }
        }
    }
}