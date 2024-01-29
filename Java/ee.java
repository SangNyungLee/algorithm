public class ee {
    public static boolean [] visited = {false,false,false,false,false,false,false,false,false};
    // 정점 1번 ~ 8번

    public static int[][] graph = {{},
            {2,3,8},
            {1,7},
            {1,4,5},
            {3,5},
            {3,4},
            {7},
            {2,6,8},
            {1,7}
    };

    public static void main(String [] args){
        int start = 1; // 시작노드
        dfs(start);
    }

    private static void dfs(int e) {
        visited[e] = true; //방문처리
        System.out.print(e + " ");
        //인접노드 탐색
        for(int i : graph[e]){
            if(!visited[i]){ //방문을 안 했으면
                dfs(i);
            }
        }
    }
}
