package ct;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class ct004 {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken()); // 2차원 배열의 크기
		int M = Integer.parseInt(st.nextToken()); // 질문 개수
		
		int arr[][] = new int[N+1][N+1];
		int arr2[][] = new int[N+1][N+1];
		
		for(int i=1; i<=N ; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=1; j<=N ; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i=1; i<=N ; i++) {
			for(int j=1 ; j<=N ; j++) {
				arr2[i][j] = arr[i][j]+arr2[i][j-1];
			}
		}
		
		
		for(int i=0; i<M ; i++) {
			int sum =0;
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());	//x1
			int b = Integer.parseInt(st.nextToken());	//y1
			int c = Integer.parseInt(st.nextToken());	//x2
			int d = Integer.parseInt(st.nextToken());	//y2
			
			for(int j=a ; j<=c ; j++) {
				sum+= arr2[j][d]-arr2[j][b-1];
			}
			
			bw.write(String.valueOf(sum) +"\n");
		}
		br.close();
		bw.flush();
	}
}