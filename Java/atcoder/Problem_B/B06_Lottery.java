import java.io.*;
import java.util.*;

public class B06_Lottery {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int [] arr = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		for(int i = 1 ; i < N + 1 ; i++){
			int a = Integer.parseInt(st.nextToken());
			if (a == 1)
				arr[i] = arr[i - 1] + 1;
			else
				arr[i] = arr[i - 1] - 1;
		}
		int Q = Integer.parseInt(br.readLine());
		for(int i = 0 ; i < Q ; i++){
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			if (arr[end] - arr[start - 1] > 0) bw.write("win\n");
			else if (arr[end] - arr[start - 1] == 0) bw.write("draw\n");
			else bw.write("lose\n");
		}
		bw.flush();
		bw.close();
	}
}
