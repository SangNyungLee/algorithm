import java.util.Scanner;

public class vvv {
    public static int n,m;
    public static int[][] graph = new int[1000][1000];
    public static boolean dfs(int x, int y){
    //범위 벗어나면 바로 종료
        if(x<= -1 || x>= n || y <= -1 || y >= m){
            return false;
        }
        // 가려는 곳이 0이면 방문한다
        if(graph[x][y] == 0){
            graph[x][y] = 1;
            // 상하좌우 탐색(재귀)
            dfs(x-1, y); //좌
            dfs(x, y - 1); // 하
            dfs(x + 1, y); // 우
            dfs(x, y+1); // 상
            return true;
        }
        return false;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        // 그래프 만들어주기
        for (int i=0 ; i<n ; i++) {
            String str = sc.next();
            for (int j = 0; j < m; j++) {
                graph[i][j] = str.charAt(j) - '0'; //str.charAt(j) - '0' 문자 -> 숫자
            }
        }
        int result = 0;
        // 탐색하기
        for(int i =0; i<n; i++){
            for(int j=0; j<m ; j++){
                //현재위치에서 dfs수행
                if(dfs(i,j)){
                    result +=1;
                }
            }
        }
        System.out.println(result);
    }

}
