import java.io.*;
import java.util.*;

public class 구간_합_구하기_5 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] arr = new int[N + 1][N + 1];
		int[][] dp = new int[N + 1][N + 1];
		for(int i = 1; i <= N ; i++){
			st = new StringTokenizer(br.readLine());
			for(int j = 1 ; j <= N ; j++)
				arr[i][j] = Integer.parseInt(st.nextToken());
		}
		for(int i = 1 ; i <= N ; i++)
			for(int j = 1 ; j <= N ; j++)
				dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j];
		
	}
}
