import java.io.*;
import java.util.*;

public class 나머지_합 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		long answer = 0;
		int sum = 0;
		int[] cnt = new int[1000];

		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < N ; i++){
			 int a = Integer.parseInt(st.nextToken());
			 sum += a;
			 sum %= M;
			 answer += cnt[sum];
			 cnt[sum]++;
			 if (sum== 0) answer++;
		}
		bw.write(Long.toString(answer));
		bw.flush();
		bw.close();
	}
}
