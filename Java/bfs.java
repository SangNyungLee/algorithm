import java.util.LinkedList;
import java.util.Queue;

public class bfs {
    public static void main(String[] args) {
        boolean [] visited = {false,false,false,false,false,false,false,false,false};
        // 정점 1번 ~ 8번
        int[][] graph = {{},
                {2,3,8},
                {1,7},
                {1,4,5},
                {3,5},
                {3,4},
                {7},
                {2,6,8},
                {1,7}
        };
        int start = 1;
        Queue<Integer> queue = new LinkedList<>();
        //시작노드 큐에 담아주기
        queue.offer(start);
        //시작노드 방문처리
        visited[start]= true;

        while(!queue.isEmpty()){
            int v = queue.poll(); // 큐에서 빼면서 변수에 담음

            for(int i : graph[v]){
                if(!visited[i]){
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}
