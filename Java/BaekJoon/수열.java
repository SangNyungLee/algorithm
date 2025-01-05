import java.io.*;
import java.util.*;

public class 수열 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int[] arr = new int[N + 1];

		st = new StringTokenizer(br.readLine());
		for(int i = 1 ; i < N + 1 ; i++)
			arr[i] = arr[i - 1] + Integer.parseInt(st.nextToken());
		int max = Integer.MIN_VALUE;
		for(int i = K ; i < N + 1 ; i++){
			int temp = arr[i] - arr[i - K];
			if (temp > max)
				max = temp;
		}
		bw.write(Integer.toString(max));
		bw.flush();
		bw.close();
	}
}
