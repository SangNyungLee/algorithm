import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());

		boolean[][] graph = new boolean[n + 1][n + 1];
		boolean[] visited = new boolean[n + 1];

		for(int i = 0 ; i < m ; i++){
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph[a][b] = true;
			graph[b][a] = true;
		}
		dfs(graph, visited, v, bw, n);
		visited = new boolean[n + 1];
		bw.write('\n');
		bfs(graph, visited, v, bw, n);
		bw.close();
	}

	public static void dfs(boolean[][] graph, boolean[] visited, int idx, BufferedWriter bw, int n) throws IOException{
		visited[idx] = true;
		bw.write(idx + " ");
		for(int i = 0 ; i < n + 1 ; i++){
			if (!visited[i] && graph[idx][i])
				dfs(graph, visited, i, bw, n);
		}
		bw.flush();
	}

	public static void bfs(boolean[][] graph, boolean[] visited, int idx, BufferedWriter bw, int n) throws IOException{
//		Queue<Integer> queue = new LinkedList<>();
		Deque<Integer> queue = new ArrayDeque<>();
		queue.add(idx);
		visited[idx] = true;
		while (!queue.isEmpty()){
			int cur = queue.poll();
			bw.write(cur + " ");
			for(int i = 0 ; i < n + 1 ; i++){
				if (!visited[i] && graph[cur][i]){
					queue.add(i);
					visited[i] = true;
				}
			}
		}
		bw.flush();
	}
}
