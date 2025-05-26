#include <utility>
#include <iostream>
#include <queue>
using namespace std;
#define X first
#define Y second
int board[502][502] =
{{1,1,1,0,1,0,0,0,0,0},
 {1,0,0,0,1,0,0,0,0,0},
 {1,1,1,0,1,0,0,0,0,0},
 {1,1,0,0,1,0,0,0,0,0},
 {0,1,0,0,0,0,0,0,0,0},
 {0,0,0,0,0,0,0,0,0,0},
 {0,0,0,0,0,0,0,0,0,0} }; // 1이 파란 칸, 0이 빨간 칸에 대응
 bool visited[502][502];
 int n = 7, m = 10;
 int dx[4] = {1, 0, -1, 0};
 int dy[4] = {0, 1, 0, -1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<pair<int, int>> queue;
    visited[0][0] = 1;
    queue.push({0,0});
    while(!queue.empty()){
        pair<int, int> cur = queue.front();
        queue.pop();
        cout << '(' << cur.X << ", " << cur.Y << ") -> ";
        for(int i = 0; i < 4 ; i++){
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (visited[nx][ny] || board[nx][ny] != 1) continue;
            visited[nx][ny] = 1;
            queue.push({nx,ny});
        }
    }
}