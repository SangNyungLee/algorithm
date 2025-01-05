import java.io.*;
import java.util.*;

public class 구간_합_구하기_4 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] arr = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1 ; i < N + 1 ; i++)
			arr[i] = arr[i - 1] + Integer.parseInt(st.nextToken());
		
		for(int i = 0 ; i < M ; i++){
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			bw.write(Integer.toString(arr[end] - arr[start - 1]) + "\n");
		}
		bw.flush();
		bw.close();
	}
}
